from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import Dish


@login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    num_users = get_user_model().objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_users": num_users,
        "num_dishes": num_dishes,
    }

    return render(request, "kitchen/index.html", context=context)
