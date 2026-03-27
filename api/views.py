from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_test(request):
    person = {"name": "test", "age": 20}
    return Response(person)
