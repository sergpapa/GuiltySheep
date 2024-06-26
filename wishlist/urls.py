# Contains Code Institute Provided Code
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('add/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('add/bag/<item_id>/', views.add_wishlist_item_to_bag, name='add_wishlist_item_to_bag'),
    path('remove/<item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),  
]