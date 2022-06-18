from django.shortcuts import render
from django.views import View
from .settings.info import *


class IndexView(View):
    def get(self, request):
        return render(request, "store/index.html", INFO)


class AboutView(View):
    def get(self, request):
        return render(request, "store/about.html")


class ShopView(View):
    def get(self, request):
        return render(request, "store/shop.html")


class CartView(View):
    def get(self, request):
        return render(request, "store/cart.html", INFO)


class WishlistView(View):
    def get(self, request):
        return render(request, "store/wishlist.html")


class CheckoutView(View):
    def get(self, request):
        return render(request, "store/checkout.html")


class SingleProductView(View):
    def get(self, request):
        return render(request, "store/product-single.html", INFO)


class ContactView(View):
    def get(self, request):
        return render(request, "store/contact.html")


class BlogView(View):
    def get(self, request):
        return render(request, "store/blog.html")


class BlogSingle(View):
    def get(self, request):
        return render(request, "store/blog-single.html")
