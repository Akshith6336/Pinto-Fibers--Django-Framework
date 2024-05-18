import random
import string
from furnitureapp.models import Cart

# Genrate random order_id
def generate_id(length=50):
    key = ""
    for i in range(length):
        key += random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
    return key


def get_cart_count(user):
    if user.is_authenticated:
        return Cart.objects.filter(user=user).count()
    return 0
