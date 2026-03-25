# Step 1 – builder
FROM python:3.14.3-bookworm AS builder
RUN apt-get update && apt-get upgrade -y
COPY --from=ghcr.io/astral-sh/uv:0.11.0 /uv /uvx /bin/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./pyproject.toml .
COPY ./uv.lock .
RUN uv sync --compile-bytecode --locked --no-dev

# Step 2 – deploy
FROM python:3.14.3-bookworm
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

WORKDIR /app
COPY --chown=appuser:appuser . .
COPY --from=builder /app/.venv/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER appuser
EXPOSE 8000
RUN chmod +x /app/entrypoint.prod.sh
ENTRYPOINT ["/app/entrypoint.prod.sh"]
