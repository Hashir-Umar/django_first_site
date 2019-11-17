from django.contrib import admin

# Register your models here.
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "author", "posted_date"]
    list_filter = ["author", "posted_date"]
    search_fields = ["author", "text"]


admin.site.register(Quote, QuoteAdmin)
