from django.urls import path

from .views import MenuView, home, AdminMenuItemCreateView


urlpatterns = [
    # path('',view=home,name='home'),
    path('',MenuView.as_view(),name='home'),
    path("menu/add/", AdminMenuItemCreateView.as_view(), name="add_menu_item"),

]