from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cpoems', views.cpoems, name="cpoems"),
    path('poems/<str:poet_cat>/', views.poems, name="poems"),
    ]