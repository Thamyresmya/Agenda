from django.contrib import admin
from core.models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')  #personalizar p/ aparecer o titulo e a data
    list_filter = ('titulo',)  #campo para filtrar, pode ser por qualquer um

admin.site.register(Evento, EventoAdmin)