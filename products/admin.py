from django.contrib import admin

from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
  list_display = ('title', 'price', 'active')


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('product', 'author', 'body', 'stars', 'active')
