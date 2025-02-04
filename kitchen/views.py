from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from kitchen.forms import DishForm
from kitchen.models import Dish, Task, Order, User


@login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    num_users = get_user_model().objects.count()
    num_dishes = Dish.objects.count()
    num_tasks = Task.objects.count()
    num_orders = Order.objects.count()

    context = {
        "num_users": num_users,
        "num_dishes": num_dishes,
        "num_tasks": num_tasks,
        "num_orders": num_orders,
    }

    return render(request, "kitchen/index.html", context=context)


class StaffListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "kitchen/staff_list.html"
    context_object_name = "staff_list"


class StaffDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "kitchen/staff_detail.html"
    context_object_name = "staff"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = kwargs.get("form", DishForm())
        context["tasks"] = Task.objects.filter(user=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.save()
            dish.users.add(form.cleaned_data["assigned_chef"])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return redirect("staff-detail", pk=self.object.pk)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
