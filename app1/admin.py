from django.contrib import admin

# Register your models here.
from .models import TodosCursos, Detalhes

admin.site.register(TodosCursos)
admin.site.register(Detalhes)

