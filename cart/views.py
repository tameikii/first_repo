from django.shortcuts import render
from django.views.generic import DetailView


from .models import Cart
# Create your views here.


class CartDetailView(DetailView):
    model = Cart
    template_name = "cart/shopping_cart.html"
