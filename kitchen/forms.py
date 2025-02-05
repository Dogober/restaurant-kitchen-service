from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Dish, User, Ingredient, Task


class DishForm(forms.ModelForm):
    assigned_chef = forms.ModelChoiceField(
        queryset=get_user_model().objects.filter(position="chef"), required=True
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
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", "position", )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
