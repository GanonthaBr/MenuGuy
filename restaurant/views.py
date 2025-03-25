from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,View
from django.http import HttpResponse

from restaurant.mixins import AdminRequiredMixin
from .models import Categories, MenuItem, CartItem
# Create your views here.

def home(request):
    return render(request,'home.html')

class MenuView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'menu.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_items"] = CartItem.objects.filter(user=self.request.user)
        context["categories"] = Categories.objects.all()
        return context
class AdminMenuItemCreateView(AdminRequiredMixin, View):
    def get(self, request):
        categories = Categories.objects.all()
        return render(request, "add_menu_item.html", {"categories": categories})
    
    def post(self, request):
        name = request.POST.get("name")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")  # Handle image upload
        category = Categories.objects.get(id=category_id)
        
        MenuItem.objects.create(name=name, price=price, category=category, image=image)
        return redirect("menu")

class CartView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = "cart.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = sum(item.item.price * item.quantity for item in self.get_queryset())
        return context
    
class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, item_id):
        item = MenuItem.objects.get(id=item_id)
        cart_item, created = CartItem.objects.get_or_create(item=item, 
                                                       user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('home')

    def remove_from_cart(request, item_id):
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return redirect('home')
        