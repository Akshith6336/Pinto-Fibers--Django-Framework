from django.shortcuts import render, redirect
from django.contrib.auth import logout
from furnitureapp.models.contact import Contact,Feedback, Service
from furnitureapp.models.product import Product,Categorie
from django.views import View
from furnitureapp.models.profile import Profile
from furnitureapp.templatetags.cart import total_cart_price
from furnitureapp import utils