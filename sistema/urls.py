from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('problema/', views.problema, name='problema'),
    path('solucao/', views.solucao, name='solucao'),
    path('autor/', views.autor, name='autor'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('toggle/<int:pk>/', views.toggle_concluir, name='toggle_concluir'),
    path('remover/<int:pk>/', views.remover, name='remover'),
]
