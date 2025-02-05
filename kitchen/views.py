from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm, StaffCreationForm, TaskForm
from kitchen.models import Dish, Task, Order, User, DishType, Category, Ingredient


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


class StaffCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    form_class = StaffCreationForm
    success_url = reverse_lazy("kitchen:staff-list")
    template_name = "kitchen/staff_form.html"


class StaffDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "kitchen/staff_detail.html"
    context_object_name = "staff"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dish_form"] = kwargs.get("dish_form", DishForm())
        context["task_form"] = kwargs.get("task_form", TaskForm())
        context["tasks"] = Task.objects.filter(user=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if "dish_form" in request.POST:
            dish_form = DishForm(request.POST)
            task_form = TaskForm()
            if dish_form.is_valid():
                dish = dish_form.save(commit=False)
                dish.save()
                dish.users.add(dish_form.cleaned_data["assigned_chef"])
                dish.ingredients.add(*dish_form.cleaned_data["assigned_ingredients"])
                return redirect("kitchen:staff-detail", pk=self.object.pk)
        elif "task_form" in request.POST:
            dish_form = DishForm()
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.save()
                return redirect("kitchen:staff-detail", pk=self.object.pk)

        else:
            dish_form = DishForm(request.POST)
            task_form = TaskForm(request.POST)

        return self.render_to_response(self.get_context_data(dish_form=dish_form, task_form=task_form))


class StaffUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = StaffCreationForm
    success_url = reverse_lazy("kitchen:staff-list")
    template_name = "kitchen/staff_form.html"


class StaffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("kitchen:staff-list")
    template_name = "kitchen/staff_confirm_delete.html"


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"
    context_object_name = "dish_type"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"
    context_object_name = "dish_type"


class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("kitchen:category-list")


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("kitchen:category-list")


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy("kitchen:category-list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    queryset = Order.objects.prefetch_related("tasks").filter(~Q(status="completed"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        task_statuses = []
        for order in self.object_list:
            statuses = [task.status for task in order.tasks.all()]
            all_completed = all(status == "completed" for status in statuses)
            task_statuses.append((order.id, all_completed))

        context["task_statuses"] = task_statuses
        return context


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    fields = "__all__"
    success_url = reverse_lazy("kitchen:order-list")


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    fields = "__all__"
    success_url = reverse_lazy("kitchen:order-list")


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("kitchen:order-list")


@login_required
def task_manager_view(request: HttpRequest, user_id: int, task_id: int) -> HttpResponse:
    task = Task.objects.get(pk=task_id)
    task.status = "completed"
    task.save()
    return redirect("kitchen:staff-detail", pk=user_id)


@login_required
def order_manager_view(request: HttpRequest, pk: int) -> HttpResponse:
    order = Order.objects.get(id=pk)
    task_statuses = [task.status for task in order.tasks.all()]
    if task_statuses and task_statuses.count("completed") == len(task_statuses):
        order.status = "completed"
        order.save()
    return redirect("kitchen:order-list")
