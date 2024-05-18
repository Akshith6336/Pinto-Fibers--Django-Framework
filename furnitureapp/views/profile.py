from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from furnitureapp.forms import CreateUserFrom, ProfileForm
from furnitureapp.models import Profile
from django.contrib import messages
from furnitureapp.middlewares.decorator import unauthentcated_user
from django.utils.decorators import method_decorator
from django.views import View
from furnitureapp.utils import get_cart_count

# Login view
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
            

#Login
@method_decorator(unauthentcated_user, name="dispatch")
class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get("return_url")
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session.pop("return_to", None) 
            if Login.return_url:
                return HttpResponseRedirect(Login.return_url)
            else:
                return redirect("/")
        else:
            messages.error(request, "Wrong password or username")
            return redirect("login")


# Profile view
@login_required(login_url="login")
def profile(request):
    # Calculate cart count
    cart_count = get_cart_count(request.user)
    return render(request, "profile.html", {"cart_count": cart_count})

# SignUp Page
def signup(request):
    form = CreateUserFrom()

    if request.method == "POST":
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account is Created")
            return redirect("login")
        else:
            context = {"form": form}
            messages.error(request, "Invalid credentials")
            return render(request, "signup.html", context)

    context = {"form": form}
    return render(request, "signup.html", context)

# UpdateProfile
@login_required(login_url="login")
def updateprofile(request):
    # Retrieve the profile or create a new one
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile is updated.")
            return redirect("profile")  # Redirect to the profile page after successful update
        else:
            print(form.errors)
            messages.error(request, "Failed to update profile. Please check the form.")
    else:
        form = ProfileForm(instance=profile)

    # Calculate cart count
    cart_count = get_cart_count(request.user)
    context = {"form": form, "cart_count": cart_count}
    return render(request, "updateprofile.html", context)


#logout
@login_required(login_url="login")
def logout_user(request):
    return_url = request.session.pop("return_to", "/")  # Get and remove return_to from session
    logout(request)
    messages.info(request, "You are logged out successfully ")
    return redirect(return_url)
