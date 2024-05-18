from django.shortcuts import redirect


def unauthentcated_user(view_func):
    def middlerware_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)

    return middlerware_func
