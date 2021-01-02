from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.proj_index, name='proj_index'),
    path('<int:pk>/', views.proj_detail, name='proj_detail'),
]