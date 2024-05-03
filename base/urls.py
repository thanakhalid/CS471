from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cpoems', views.cpoems, name="cpoems"),
    path('poems/<str:poet_cat>/', views.poems, name="poems"),
    path('poem/<int:poem_id>/', views.poem, name="poem"),
    path('add_comment/<int:poem_id>/', views.add_comment, name="add_comment"),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),


    ]