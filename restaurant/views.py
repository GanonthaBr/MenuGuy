from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,View
from restaurant.mixins import AdminRequiredMixin
from .models import Categories, MenuItem, CartItem,Order, OrderItem
# Create your views here.

class MenuView(LoginRequiredMixin,ListView):
    model = Categories
    template_name = "menu.html"
    context_object_name = "categories"

    def get_number(self,**kwargs):
        total=0
        items = CartItem.objects.filter(user=self.request.user)
        for i in items:
            total += 1
        return total

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_category = self.request.GET.get("categories", "all")
        
        if selected_category == "all":
            menu_items = MenuItem.objects.all()
        else:
            menu_items = MenuItem.objects.filter(categories__id=selected_category)
        
        context["cart_items"] = CartItem.objects.filter(user=self.request.user)
        context["menu_items"] = menu_items
        context['number'] =   self.get_number()
        context["selected_category"] = selected_category
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

  

class IncreaseQuantityView(LoginRequiredMixin, View):
    def get(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect("cart")
        
class DecreaseQuantityView(LoginRequiredMixin, View):

    def get(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect("cart")

class RemoveCartItemView(LoginRequiredMixin, View):
    def get(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        cart_item.delete()
        return redirect("cart")
    

class PlaceOrderView(View):
    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        # print(cart_items)
        if not cart_items.exists():
            return redirect("cart")  # Prevent empty orders
        order = Order.objects.create(user=request.user)
        
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity
            )
        order.calculate_total()
        order.save() 

        
        # Clear cart after placing order
        cart_items.delete()
        
        return redirect("home")

class OrderDetailView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id, user=request.user)
        return render(request, "order_detail.html", {"order": order})