from django.contrib import admin

from .models import Category, Photo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'uploaded_at')
    list_filter = ('category', 'uploaded_at')
    search_fields = ('title', 'description')
