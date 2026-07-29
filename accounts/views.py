from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy

from .forms import LoginForm, RegistrationForm


# Create your views here.


class StudentLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "accounts/login.html"


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)

        student_group = Group.objects.get(name="Student")
        self.object.groups.add(student_group)

        messages.success(
            self.request,
            "Account created successfully. Please log in."
        )

        return response
