from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "name",
                    "course",
                    "age",
                    "email",
                    "roll_number",
                    )

    search_fields = (
        "name",
        "roll_number",
        "course"
    )

    list_filter = (
        "course",
        "age",
        "id"
    )

    ordering = ("roll_number",)
