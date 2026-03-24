from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)


class RSSFeed(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_fetched = models.DateTimeField(null=True, blank=True)
    error_count = models.IntegerField(default=0)  # type: ignore


class Article(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(unique=True)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(RSSFeed, on_delete=models.CASCADE)


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Article, related_name="favorited_by")
    subscriptions = models.ManyToManyField(RSSFeed, related_name="subscribers")
