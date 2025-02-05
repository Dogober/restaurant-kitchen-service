from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Dish, User


class DishForm(forms.ModelForm):
    assigned_chef = forms.ModelChoiceField(
        queryset=get_user_model().objects.filter(position="chef"), required=True
    )

    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
            "ingredients",
            "assigned_chef",
        ]

class StaffCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", "position", )
