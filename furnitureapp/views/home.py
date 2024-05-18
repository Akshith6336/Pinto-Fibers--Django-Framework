from django.shortcuts import render, redirect
from furnitureapp.models.product import Product, Categorie
from furnitureapp.models import Cart
from django.contrib.auth.decorators import login_required
from django.views import View
from furnitureapp.utils import get_cart_count  # Import get_cart_count function

# Home
class home(View):
    def get(self, request):
        products = Product.get_all_products()
        cart_count = get_cart_count(request.user)  # Calculate cart count
        data = {"products": products, "cart_count": cart_count }
        return render(request, "home.html", data)

    def post(self, request):
        if request.user.is_authenticated:
            product_id = request.POST.get("product")
            remove = request.POST.get("remove")
            if product_id:
                product = Product.objects.get(pk=product_id)
                user_cart, created = Cart.objects.get_or_create(user=request.user, product=product)
                if remove:
                    if user_cart.product_qty <= 1:
                        user_cart.delete()
                    else:
                        user_cart.product_qty -= 1
                        user_cart.save()
                else:
                    user_cart.product_qty += 1
                    user_cart.save()
            return redirect("home")
        else:
            return redirect("login") 

# Product
class product(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Categorie.objects.all()
        category_id = request.GET.get("category")
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        cart_count = get_cart_count(request.user)  # Calculate cart count
        context = {"products": products, "categories": categories, "cart_count": cart_count}
        return render(request, "product.html", context)

    def post(self, request):
        if request.user.is_authenticated:
            product_id = request.POST.get("product")
            remove = request.POST.get("remove")
            if product_id:
                product = Product.objects.get(pk=product_id)
                user_cart, created = Cart.objects.get_or_create(user=request.user, product=product)
                if remove:
                    if user_cart.product_qty <= 1:
                        user_cart.delete()
                    else:
                        user_cart.product_qty -= 1
                        user_cart.save()
                else:
                    user_cart.product_qty += 1
                    user_cart.save()
            return redirect("product")
        else:
            return redirect("login")  
