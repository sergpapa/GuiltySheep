
from django.contrib import admin
from .models import Product, Category, Collection, Artist, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name"
    )

class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name"
    )

class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name"
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "user",
        "review_title",
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Review, ReviewAdmin)
