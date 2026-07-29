from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("add/", views.StudentCreateView.as_view(), name="add_student"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="update_student"),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="delete_student"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
]
