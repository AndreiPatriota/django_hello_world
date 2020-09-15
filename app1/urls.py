from django.urls import path
from . import views

urlpatterns = [
    path('<int:id_curso>/', views.detalhe, name = 'detalhes'),
    path('', views.cursos, name = 'Minha Página'),
]
