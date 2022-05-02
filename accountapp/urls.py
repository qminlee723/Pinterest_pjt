from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import hello_world, AccountCreateView

app_name = 'accountapp'
urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
]
