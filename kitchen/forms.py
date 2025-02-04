from django import forms
from django.contrib.auth import get_user_model

from .models import Dish


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
