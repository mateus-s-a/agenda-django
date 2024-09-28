from django.contrib import admin

from agenda.models import Evento, Categoria

# REGISTRA MODELOS PARA SEREM ACESSADOS ATRAVÉS DE ADMINISTRAÇÃO DO DJANGO
# Register your models here.
admin.site.register(Evento)
admin.site.register(Categoria)