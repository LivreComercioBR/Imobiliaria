from django.contrib import admin
from plataforma.models import Imagem, Cidade, Bairro, DiasVisita, Horario, Imovel, Visitas


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('rua', 'cidade', 'bairro', 'valor', 'tamanho', 'quartos', 'tipo',)
    list_editable = ('valor', 'tipo',)
    list_filter = ('cidade', 'tipo',)


# Register your models here.
admin.site.register(Imagem)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Visitas)
