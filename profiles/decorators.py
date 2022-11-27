from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Profile

# Unauthenticate User Check
def unauthenticate_user(view_func):
    def authenticate_wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index_view')
        else:
            return view_func(request, *args, **kwargs)
    return authenticate_wrap