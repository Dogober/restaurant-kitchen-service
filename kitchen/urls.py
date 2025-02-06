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
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    task_manager_view,
    order_manager_view,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    sign_up_view,
)

urlpatterns = [
    path("", index, name="home-page"),
    path("staff/", StaffListView.as_view(), name="staff-list"),
    path("staff/create/", StaffCreateView.as_view(), name="staff-create"),
    path("staff/<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),
    path(
        "staff/<int:pk>/update/",
        StaffUpdateView.as_view(),
        name="staff-update",
    ),
    path(
        "staff/<int:pk>/delete/",
        StaffDeleteView.as_view(),
        name="staff-delete",
    ),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/create/",
        CategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path(
        "ingredients/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/create/", OrderCreateView.as_view(), name="order-create"),
    path(
        "orders/<int:pk>/update/",
        OrderUpdateView.as_view(),
        name="order-update",
    ),
    path(
        "orders/<int:pk>/delete/",
        OrderDeleteView.as_view(),
        name="order-delete",
    ),
    path(
        "staff/<int:user_id>/<int:task_id>/",
        task_manager_view,
        name="task-manager",
    ),
    path("orders/<int:pk>/", order_manager_view, name="order-manager"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"
    ),
    path("sign_up/", sign_up_view, name="sign-up"),
]

app_name = "kitchen"
