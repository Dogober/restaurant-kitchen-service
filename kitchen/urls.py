from django.urls import path

from .views import index, StaffListView, StaffDetailView

urlpatterns = [
    path("", index, name="home-page"),
    path("staff/", StaffListView.as_view(), name="staff-list"),
    path("staff/<int:pk>/", StaffDetailView.as_view(), name="staff-detail")
]

app_name = "kitchen"
