from django.shortcuts import redirect


# Middleware
def auth_middleware(get_response):
    def middleware(request):
        if not request.user.is_authenticated:
            returnUrl = request.META["PATH_INFO"]
            if not request.session.get("customer_id"):
                request.session["return_to"] = returnUrl
                return redirect(f"login?return_url={returnUrl}")
        else:
            request.session["return_to"] = (
                request.path
            )  # Set return_to to the current URL for authenticated users
        response = get_response(request)
        return response

    return middleware
