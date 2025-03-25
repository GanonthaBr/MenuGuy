from django.contrib import admin
from .models import CartItem, Categories, MenuItem,Order
from account.models import User

# Register your models here.
from django.contrib import admin
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "My Custom Admin"
    site_title = "Admin Panel"
    index_title = "Welcome to My Admin Panel"

admin_site = MyAdminSite()

# Register styles and scripts
admin.site.site_url = None  # Remove "View Site" link

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("admin/css/custom.css",)}
        js = ("admin/js/custom.js",)

# Apply to models

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

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',  'display_items']

    def display_items(self, obj):
        return ", ".join([str(item) for item in obj.items.all()])
    display_items.short_description = 'Items'
#resgister the model classes
admin_site.register(MenuItem, MenuItemAdmin)
admin_site.register(Categories, CategoriesAdmin)
admin_site.register(CartItem, CartItemAdmin)
admin_site.register(Order,OrderAdmin)


