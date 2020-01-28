from django.urls import path
from . import views

urlpatterns = [
    path('', views.help, name='help'),
    path('inner_path/', views.inner, name='inner')
]