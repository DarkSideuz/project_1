from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'created_at')
    search_fields = ('name', 'description', 'category__name')
    list_filter = ('category',)