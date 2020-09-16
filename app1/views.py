from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import TodosCursos
from django.template import loader

# Create your views here.
def cursos(request):
    ac = TodosCursos.objects.all()

    return render(request, 'app1/cursos.html', {'ac': ac})


def detalhe(request, id_curso):
    curso = get_object_or_404(TodosCursos, pk=id_curso)
    return render(request, 'app1/detalhe.html', {'curso':curso})


def escolha(request, id_curso):
    curso = get_object_or_404(TodosCursos, pk=id_curso)
    try:
        selected_tipo = curso.detalhes_set.get(pk=request.POST['choice'])
    except (KeyError, TodosCursos.DoesNotExist):
        render(request, 'app1/detalhe.html', {'curso':curso, 'error_mens':'selecione uma opção válida!'})
    else:
        selected_tipo.your_choice=True
        selected_tipo.save()
        return render(request, 'app1/detalhe.html', {'curso':curso})
