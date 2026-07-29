from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import StudentLoginView, RegisterView

urlpatterns = [
    path('login/', StudentLoginView.as_view(),
         name='login'),
    path('logout/', LogoutView.as_view(),
         name='logout'),
    path('register/', RegisterView.as_view(),
         name='register')
]