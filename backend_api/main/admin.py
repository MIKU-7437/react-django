from django.contrib import admin
from . import models


admin.site.register(models.Vendor)
admin.site.register(models.ProductCategory)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderProduct)
admin.site.register(models.CustomerAddress)
admin.site.register(models.ProductRating)
admin.site.register(models.ProductImage)

class ProductImageInline(admin.StackedInline):
    model = models.ProductImage

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title', ]}
    inlines = [
        ProductImageInline,
    ]
admin.site.register(models.Product, ProductAdmin)