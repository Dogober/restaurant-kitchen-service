from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Dish, User, Ingredient, Task


class DishForm(forms.ModelForm):
    assigned_chef = forms.ModelChoiceField(
        queryset=get_user_model().objects.filter(position="chef"),
        required=True,
    )
    assigned_ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
            "assigned_ingredients",
            "assigned_chef",
        ]


class StaffCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
            "position",
        )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class IngredientSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class StaffSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class CategorySearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[("", "All")] + Task.STATUS_CHOICES,
        required=False,
        label="Status",
        widget=forms.Select(
            attrs={
                "class": "custom-select",
            }
        )
    )
    username = forms.ChoiceField(
        required=False,
        label="Chef Username",
        choices=[
            (user.username, user.username) for user in User.objects.all()
        ],
        widget=forms.Select(attrs={"class": "custom-select"})
    )
