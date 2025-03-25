from django.urls import path

from .views import MenuView, AdminMenuItemCreateView, AddToCartView,CartView,RemoveCartItemView,DecreaseQuantityView,IncreaseQuantityView,OrderDetailView,PlaceOrderView


urlpatterns = [
    # path('',view=home,name='home'),
    path('',MenuView.as_view(),name='home'),
    path("menu/add/", AdminMenuItemCreateView.as_view(), name="add_menu_item"),
    path("add-to-cart/<int:item_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path("remove/<int:item_id>/", RemoveCartItemView.as_view(), name="remove_cart_item"),
    path("decrease/<int:item_id>/", DecreaseQuantityView.as_view(), name="decrease_quantity"),
    path("increase/<int:item_id>/", IncreaseQuantityView.as_view(), name="increase_quantity"),
    path("cart/", CartView.as_view(), name="cart"),
    path("place_order/", PlaceOrderView.as_view(), name="place_order"),
    path("order/<int:order_id>/", OrderDetailView.as_view(), name="order_detail"),
]