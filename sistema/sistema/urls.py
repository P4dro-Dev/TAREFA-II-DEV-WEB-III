from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('problema/', views.problema, name='problema'),
    path('solucao/', views.solucao, name='solucao'),
    path('autor/', views.autor, name='autor'),
]
