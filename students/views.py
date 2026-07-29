from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView,
                                  TemplateView, DetailView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request, "students/home.html")


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Student
    template_name = "students/student_list.html"
    permission_required = "students.view_student"
    context_object_name = "students"
    paginate_by = 3

    def get_queryset(self):
        queryset = Student.objects.all().order_by("-id")

        query = self.request.GET.get("q")

        if query:
            if query.isdigit():
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(course__icontains=query) |
                    Q(email__icontains=query) |
                    Q(roll_number=int(query))
                )
            else:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(course__icontains=query) |
                    Q(email__icontains=query)
                )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["query"] = self.request.GET.get("q", "")
        return context


# def student_list(request):
#
#     query = request.GET.get("q")
#
#     students = Student.objects.all().order_by("roll_number")
#
#     if query:
#         if query.is_digit():
#             students = students.filter(
#                 Q(name__icontains=query) |
#                 Q(course__icontains=query) |
#                 Q(email__icontains=query) |
#                 Q(roll_number=int(query))
#             )
#         else:
#             students = students.filter(
#                 Q(name__icontains=query) |
#                 Q(course__icontains=query) |
#                 Q(email__icontains=query)
#             )
#     paginator = Paginator(students, 3)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         "page_obj": page_obj,
#         "query": query
#     }
#
#     return render(request, "students/student_list.html", context)


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    permission_required = "students.add_student"
    success_url = reverse_lazy("student_list")
    template_name = "students/add_student.html"

    def form_valid(self, form):
        messages.success(self.request, "Student Added Successfully!")
        return super().form_valid(form)


# def add_student(request):
#
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, "Student Added Successfully!")
#
#             return redirect("student_list")
#     else:
#         form = StudentForm()
#
#     return render(request, "students/add_student.html", {"form": form})


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    permission_required = "students.change_student"
    success_url = reverse_lazy("student_list")
    template_name = "students/update_student.html"

    def form_valid(self, form):
        messages.success(self.request, "Student Updated Successfully!")
        return super().form_valid(form)

    # pk_url_kwarg = "id" # do this <- or change int:pk instead of int:id in urls.py


# def update_student(request, id):
#
#     student = get_object_or_404(Student, id=id)
#
#     if request.method == "POST":
#         form = StudentForm(
#             request.POST,
#             instance=student
#         )
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, "Student Updated Successfully!")
#
#             return redirect("student_list")
#     else:
#         form = StudentForm(
#             instance=student
#         )
#     return render(request, "students/update_student.html", {"form": form})


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    permission_required = "students.delete_student"
    template_name = "students/delete_student.html"
    success_url = reverse_lazy("student_list")
    raise_exception = True
    def form_valid(self, form):
        messages.success(self.request, "Student Deleted Successfully!")
        return super().form_valid(form)


# def delete_student(request, id):
#     student = get_object_or_404(Student, id=id)
#
#     if request.method == "POST":
#         student.delete()
#
#         messages.success(request, "Student Deleted Successfully!")
#
#         return redirect("student_list")
#
#     context = {
#         "student": student
#     }
#
#     return render(request, "students/delete_student.html", context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "students/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_students"] = Student.objects.count()

        context["total_courses"] = Student.objects.values(
            "course"
        ).distinct().count()

        context["recent_students"] = Student.objects.order_by("-id")[:5]

        context["course_data"] = Student.objects.values("course").annotate(
            total=Count("id")
        )

        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"
    context_object_name = "student"

