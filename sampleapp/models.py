from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='poster')
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)


class Reels(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Main_slidebar(models.Model):
    Mainslidebar = models.ImageField(upload_to='Main_slidebar')

class Second_slidebar(models.Model):
    second_slidebar = models.ImageField(upload_to='Second_slidebar')

class Third_slidebar(models.Model):
    Third_slidebar = models.ImageField(upload_to='Third_slidebar')