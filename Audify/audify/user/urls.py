from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='user-home'),
    # path("login", views.login_request, name="login")
]