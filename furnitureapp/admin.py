from django.contrib import admin
from .models.profile import Profile
from .models.product import Product, Categorie
from .models.contact import Contact, Feedback, Service
from .models.orders import Order, OrderItem
from .models.cart import Cart

# Register your models here.
# admin.site.register(Service)
admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)
