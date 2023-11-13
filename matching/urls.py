from django.urls import path
from . import views

app_name = "matching"

urlpatterns = [
  path('', views.index, name='index'),
  path('dm/<int:id>', views.dm, name='dm'),
  # path('delete/<int:id>/', delete, name='delete'),
]
