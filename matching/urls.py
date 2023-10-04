from django.urls import path
from . import views

app_name = "matching"

urlpatterns = [
  path('', views.index, name='index'),
  # path('delete/<int:id>/', delete, name='delete'),
]
