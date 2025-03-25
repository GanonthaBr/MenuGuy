from django.urls import path

from .views import MenuView, AdminMenuItemCreateView, AddToCartView,CartView


urlpatterns = [
    # path('',view=home,name='home'),
    path('',MenuView.as_view(),name='home'),
    path("menu/add/", AdminMenuItemCreateView.as_view(), name="add_menu_item"),
    path("add-to-cart/<int:item_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path("remove/<int:item_id>/", AddToCartView.as_view(), name="remove"),
    path("cart/", CartView.as_view(), name="cart"),
]