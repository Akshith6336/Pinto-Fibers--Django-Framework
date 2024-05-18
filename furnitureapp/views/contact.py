from django.shortcuts import render, redirect
from furnitureapp.models.contact import Contact, Feedback
from django.views import View
import random
from furnitureapp.utils import get_cart_count


# Contact
class contact(View):
    def get(self, request):
        cart_count = get_cart_count(request.user)
        context = {"cart_count": cart_count}
        return render(request, "contact.html", context)

    def post(self, request):
        name = request.POST.get("name")
        phone_number = request.POST.get("phone")
        email = request.POST.get("email")
        description = request.POST.get("description")
        contact = Contact(
            name=name, phone_number=phone_number, email=email, description=description
        )
        contact.save()

        cart_count = get_cart_count(request.user)

        message = "Thank you for contacting us! We have received your message and will get back to you as soon as possible."
        context = {"cart_count": cart_count, "message": message}
        return render(request, "contact.html", context)


# Feedback
class feedback(View):
    def get(self, request):
        cart_count = get_cart_count(request.user)
        context = {"cart_count": cart_count}
        return render(request, "feedback.html", context)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        description = request.POST.get("desc")
        feedback = Feedback(name=name, email=email, feedback_description=description)
        feedback.save()

        # Get the cart count again
        cart_count = get_cart_count(request.user)
        message = "Your feedback has been saved."
        context = {"cart_count": cart_count, "message": message}
        return render(request, "feedback.html", context)


# Genrate random color from RGB
def generate_light_color():
    r = random.randint(180, 255)
    g = random.randint(180, 255)
    b = random.randint(180, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


# Services
# def service(request):
#     cart_count = get_cart_count(request.user)
#     services = Service.get_all_sevices()
#     service_data = []

#     for service in services:
#         service_name_hash = abs(hash(service.service_name)) % 16777215
#         text_color = generate_light_color()
#         background_color = generate_light_color()
#         service_data.append(
#             {
#                 "service": service,
#                 "service_name_hash": service_name_hash,
#                 "text_color": text_color,
#                 "background_color": background_color,
#             }
#         )

#     context = {"services": service_data, "cart_count": cart_count}
#     return render(request, "service.html", context)


# About
def about(request):
    # Add cart count to the context
    cart_count = get_cart_count(request.user)
    context = {"cart_count": cart_count}
    return render(request, "about.html", context)
