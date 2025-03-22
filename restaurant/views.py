from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,View
from django.http import HttpResponse
from .models import Categories, MenuItem, CartItem
# Create your views here.

def home(request):
    return render(request,'home.html')

class MenuView(ListView):
    model = MenuItem
    template_name = 'menu.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_items"] = CartItem.objects.filter(user=self.request.user)
        context["categories"] = Categories.objects.all()
        return context

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