from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import (
    DishType,
    User,
    Category,
    Ingredient,
    Dish,
    Order,
    Task,
)

admin.site.register(DishType)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "years_of_experience",
        "position",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "years_of_experience",
                        "position",
                    )
                },
            ),
        )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                        "position",
                    )
                },
            ),
        )
    )


admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(Task)
