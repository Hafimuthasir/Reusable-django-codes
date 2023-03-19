# decorator structure example

# decorators.py
from django.http import HttpResponseForbidden
from rest_framework.response import Response

def require_admin(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            return HttpResponseForbidden('You must be an admin to access this page')
        return view_func(request, *args, **kwargs)
    return wrapper


# views.py
from .decorators import require_admin

@require_admin
def view_func(request):
    # functios here..........
    # .......................
    return Response
