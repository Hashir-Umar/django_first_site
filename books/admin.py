from django.contrib import admin

# Register your models here.
from books.models import Book, Profile, Author, Tag

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Profile)
