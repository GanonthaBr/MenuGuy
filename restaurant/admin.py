from django.contrib import admin
from .models import CartItem, Categories, MenuItem

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity')

#resgister the model classes
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(CartItem, CartItemAdmin)

