from django.shortcuts import render, redirect
from furnitureapp.templatetags.cart import total_cart_price
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from furnitureapp.models.product import Product
from furnitureapp.models.profile import Profile
from django.http import JsonResponse
from furnitureapp.models.orders import Order, OrderItem
from django.conf import settings
from django.contrib import messages
import random
from furnitureapp.models import Cart
from furnitureapp.utils import get_cart_count  #


@login_required(login_url="login")
def checkout(request):
    if request.method == "GET":
        # Calculate cart count
        cart_count = get_cart_count(request.user)

        cart_items = Cart.objects.filter(user=request.user)
        products = [item.product for item in cart_items]

        userprofile = Profile.objects.filter(user=request.user).first()
        context = {
            "products": products,
            "userprofile": userprofile,
            "cart_items": cart_items,
            "cart_count": cart_count,
        }  # Pass cart_count to the context
        return render(request, "checkout.html", context)


@login_required(login_url="login")
def placeorder(request):
    if request.method == "POST":
        # Calculate cart count
        cart_count = get_cart_count(request.user)

        # Update user's first name and last name if they are not already set
        currentuser = User.objects.get(id=request.user.id)
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get("fname")
            currentuser.last_name = request.POST.get("lname")
            currentuser.save()

        # Check if the user has a profile, and create/update it accordingly
        try:
            userprofile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            userprofile = Profile(user=request.user)

        userprofile.phone = request.POST.get("phone")
        userprofile.address = request.POST.get("address")
        userprofile.city = request.POST.get("city")
        userprofile.state = request.POST.get("state")
        userprofile.country = request.POST.get("country")
        userprofile.pincode = request.POST.get("pincode")
        userprofile.save()

        # Create a new order
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get("fname")
        neworder.lname = request.POST.get("lname")
        neworder.email = request.POST.get("email")
        neworder.phone = request.POST.get("phone")
        neworder.address = request.POST.get("address")
        neworder.city = request.POST.get("city")
        neworder.state = request.POST.get("state")
        neworder.country = request.POST.get("country")
        neworder.pincode = request.POST.get("pincode")
        neworder.payment_mode = request.POST.get("payment_mode")
        neworder.payment_id = request.POST.get("payment_id")

        # Retrieve cart items from the database
        cart_items = Cart.objects.filter(user=request.user)
        products = [item.product for item in cart_items]
        cart_total_price = total_cart_price(products, cart_items)

        neworder.total_price = cart_total_price

        trackno = "sharma" + str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=trackno).exists():
            trackno = "sharma" + str(random.randint(1111111, 9999999))
        neworder.tracking_no = trackno
        neworder.save()

        # Create order items
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=neworder,
                product=cart_item.product,
                product_id=cart_item.product.id,
                product_image_url=cart_item.product.image.url,
                price=cart_item.product.price,
                quantity=cart_item.product_qty,
            )

        cart_items.delete()
        messages.success(request, "Your order has been placed successfully")

        payMode = request.POST.get("payment_mode")
        if payMode == "Paid by Razorpay":
            return JsonResponse({"status": "Your order has been placed successfully"})

    messages.success(request, "Your order has been placed successfully")
    return redirect("orders")


def razorpaycheck(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    products = [item.product for item in cart_items]
    cart_total_price = total_cart_price(products, cart_items)
    print(cart_total_price)
    return JsonResponse({"total_price": cart_total_price})
