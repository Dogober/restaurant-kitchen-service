from django.urls import path

from .views import (
    index,
    StaffListView,
    StaffCreateView,
    StaffDetailView,
    StaffUpdateView,
    StaffDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", index, name="home-page"),
    path("staff/", StaffListView.as_view(), name="staff-list"),
    path("staff/create/", StaffCreateView.as_view(), name="staff-create"),
    path("staff/<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),
    path("staff/<int:pk>/update/", StaffUpdateView.as_view(), name="staff-update"),
    path("staff/<int:pk>/delete/", StaffDeleteView.as_view(), name="staff-delete"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
]

app_name = "kitchen"
