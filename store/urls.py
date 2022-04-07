from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('shop/', ShopView.as_view(), name="shop"),
    path('cart/', CartView.as_view(), name="cart"),
    path('wishlist/', WishlistView.as_view(), name="wishlist"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('single_product/', SingleProductView.as_view(), name="single_product"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('contact/', ContactView.as_view(), name="contact"),
]
