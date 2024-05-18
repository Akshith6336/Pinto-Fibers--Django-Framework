from django.urls import path
from .views.home import home, product
from .views.cart import cart
from .views.contact import contact, feedback, about
from .views.profile import Login, profile, logout_user, signup, updateprofile
from .views.orders import order_view, orderview
from .views.checkout import razorpaycheck, placeorder, checkout
from .views.resetPassword import changepassword, forgetpassword
from .middlewares.auth import auth_middleware

urlpatterns = [
    path("", home.as_view(), name="home"),
    path("about", about, name="about"),
    # path("service", service, name="service"),
    path("product", product.as_view(), name="product"),
    path("contact", contact.as_view(), name="contact"),
    path("feedback", auth_middleware(feedback.as_view()), name="feedback"),
    path("cart", auth_middleware(cart), name="cart"),
    path("signup", signup, name="signup"),
    path("login", Login.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("updateprofile/", updateprofile, name="updateprofile"),
    path("profile-/", profile, name="profile"),
    path("orders", order_view, name="orders"),
    path("view-order/<str:t_no>", orderview, name="orderview"),
    path("forget-password/", forgetpassword, name="forgetpassword"),
    path("change-password/<token>/", changepassword, name="changepassword"),
    path("checkout", auth_middleware(checkout), name="checkout"),
    path("place-order", placeorder, name="placeorder"),
    path("proceed-to-pay", razorpaycheck, name="razorpaycheck"),
]
