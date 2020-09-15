from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import TodosCursos
from django.template import loader

# Create your views here.
def cursos(request):
    ac = TodosCursos.objects.all()

    return render(request, 'app1/cursos.html', {'ac': ac})


def detalhe(request, id_curso):
    try:
        curso = TodosCursos.objects.get(pk=id_curso)
    except TodosCursos.DoesNotExist:
        raise Http404(f'Curso não existe!')
    else:
        return render(request, 'app1/detalhe.html', {'curso': curso})