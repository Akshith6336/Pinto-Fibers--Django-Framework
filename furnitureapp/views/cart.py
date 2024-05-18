from django.shortcuts import render, redirect
from furnitureapp.models import Product, Cart
from django.contrib.auth.decorators import login_required
from furnitureapp.utils import get_cart_count 

def cart(request):
    cart_count = get_cart_count(request.user)
    if request.method == "GET":
        cart_items = Cart.objects.filter(user=request.user)
        products = [item.product for item in cart_items]
        return render(request, "cart.html", {"products": products, "cart_items": cart_items, "cart_count": cart_count})
    
    elif request.method == "POST":
        product_id = request.POST.get("product")
        remove = request.POST.get("remove")
        
        if product_id:
            product = Product.objects.get(pk=product_id)
            cart_item = Cart.objects.filter(user=request.user, product=product).first()
            
            if remove:  
                cart_item.delete()
            else:
                cart_item.product_qty += 1
                cart_item.save()
        
        return redirect("cart")