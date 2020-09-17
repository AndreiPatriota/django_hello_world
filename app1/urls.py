from django.urls import path
from . import views

app_nome = 'app1'

urlpatterns = [
    path('<int:id_curso>/', views.detalhe, name = 'detalhes'),
    path('', views.cursos, name = 'Minha Página'),
    path('<int:id_curso>/escolha/', views.escolha, name = 'escolha'),
]
