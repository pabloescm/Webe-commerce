from django.contrib import admin
from .models.category import Category

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
