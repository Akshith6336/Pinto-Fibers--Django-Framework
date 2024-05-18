from django.shortcuts import render
from furnitureapp.models.orders import Order, OrderItem
from django.contrib.auth.decorators import login_required
from furnitureapp.utils import get_cart_count
from furnitureapp.middlewares.auth import auth_middleware


# @auth_middleware
@login_required(login_url="login")
def order_view(request):
    # Calculate cart count
    cart_count = get_cart_count(request.user)

    orders = Order.objects.filter(user=request.user)
    context = {
        "orders": orders,
        "cart_count": cart_count,
    }  # Pass cart_count to the context
    return render(request, "orders.html", context)


@login_required(login_url="login")
def orderview(request, t_no):
    # Calculate cart count
    cart_count = get_cart_count(request.user)

    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    order_items = OrderItem.objects.filter(order=order)
    context = {
        "order": order,
        "orderitems": order_items,
        "cart_count": cart_count,
    }  # Pass cart_count to the context
    return render(request, "view-order.html", context)
