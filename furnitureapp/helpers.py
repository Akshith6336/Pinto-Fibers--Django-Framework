# helpers.py
from django.core.mail import send_mail
from django.conf import settings
import requests


def send_forget_password_mail(email, token):
    subject = "Your forget password link"
    message = f"Hi, click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

    # Disable SSL certificate verification (for local testing only)
    response = requests.post("http://127.0.0.1:8000/forget-password/", verify=False)
