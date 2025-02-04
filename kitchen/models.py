from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]


class User(AbstractUser):
    POSITION_CHOICES = [
        ("chef", "Can cook and create tasks for other cooks"),
        ("waiter", "Can only bring orders"),
    ]

    years_of_experience = models.IntegerField(null=True)
    position = models.CharField(max_length=6, choices=POSITION_CHOICES, default="chef")


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["name"]


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    class Meta:
        ordering = ["name"]

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Is pending"),
        ("in_progress", "Is in the process"),
        ("completed", "Is completed"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    dishes = models.ManyToManyField(Dish, related_name="orders")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="pending")

    class Meta:
        ordering = ["created_at"]

class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Is pending"),
        ("in_progress", "Is in the process"),
        ("completed", "Is completed"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="tasks")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="tasks")
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="pending")

    class Meta:
        unique_together = ("dish", "user", "order")
        ordering = ["created_at"]

        # Ensures that a chef cannot have more than one task
        # per dish within a single order.
