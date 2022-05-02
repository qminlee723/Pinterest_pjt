from django.urls import path
from . import views
from .views import AccountCreateView

app_name = 'accountapp'
urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name = 'create'),
]