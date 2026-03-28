from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from core.models import Category, RSSFeed, AppUser, Article
from .serializers import CategorySerilizer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endropint for edit and view category
    """

    queryset = Category.objects.all()
    serializer_class = Category
    permission_classes = [permissions.IsAuthenticated]
