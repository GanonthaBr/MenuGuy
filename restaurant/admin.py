from django.contrib import admin
from .models import CartItem, Categories, MenuItem
from account.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','phone']

admin.site.register(User,UserAdmin)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description','image_preview']

    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="50" height="50"/>' if obj.image else "No Image"


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']

#resgister the model classes
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(CartItem, CartItemAdmin)

