from django.urls import path

from .views import MenuView, home


urlpatterns = [
    path('',view=home,name='home'),
    path('menu/',MenuView.as_view(),name='menu'),

]