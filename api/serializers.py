from rest_framework import serializers
from core.models import Category, RSSFeed, Article, AppUser


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
