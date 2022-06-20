from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage
from .settings.info import *
from .settings.db import *


class IndexView(View):
    def get(self, request):
        return render(request, "store/index.html", INFO)


class AboutView(View):
    def get(self, request):
        return render(request, "store/about.html", INFO)


class ShopView(View):
    def get(self, request, page=1):
        paginator = Paginator(PRODUCT_LIST, PRODUCTS_ON_PAGE)
        try:
            products = paginator.page(page)
        except EmptyPage:
            return redirect(reverse("shop"))
        data = {"products": products, "current_page": page, "num_pages": paginator.page_range, "info": INFO}

        return render(request, "store/shop.html", data)


class CartView(View):
    def get(self, request):
        return render(request, "store/cart.html", INFO)


class WishlistView(View):
    def get(self, request):
        return render(request, "store/wishlist.html", INFO)


class CheckoutView(View):
    def get(self, request):
        return render(request, "store/checkout.html", INFO)


class SingleProductView(View):
    def get(self, request):
        return render(request, "store/product-single.html", INFO)


class ContactView(View):
    def get(self, request):
        return render(request, "store/contact.html", INFO)


class BlogView(View):
    def get(self, request):
        return render(request, "store/blog.html", INFO)


class BlogSingle(View):
    def get(self, request):
        return render(request, "store/blog-single.html", INFO)
