from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class Profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Author(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="author")


class Book(models.Model):
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField('date published')
    books = models.ForeignKey(Author, on_delete=models.CASCADE,  related_name="author")

