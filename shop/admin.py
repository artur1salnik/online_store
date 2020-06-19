from django.contrib import admin
from .models import Category, Product


# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    # inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)


# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductImage._meta.fields]
#
#     class Meta:
#         model = ProductImage
#
#
# admin.site.register(ProductImage, ProductImageAdmin)

