from django.contrib import admin
from .models import Locador,Locatario,Imovel,Contrato,Pagamento

@admin.register(Locador)
class locadorAdmin(admin.ModelAdmin):
    list_dysplay = ('id','nome','email')

@admin.register(Locatario)
class locatarioAdmin(admin.ModelAdmin):
    list_dysplay = ('id','nome','telefone')

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'endereco', 'valor_mensal', 'locador')
    list_filter = ('tipo',)
    
    search_fields = ('endereco',)
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('locador', 'locatario', 'imovel', 'data_inicio', 'data_fim', 'valor')
    list_filter = ('data_inicio', 'data_fim')
    search_fields = ('locador__nome', 'locatario__nome', 'imovel__endereco')
    
@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'data_pagamento', 'valor_pago', 'metodo')
    list_filter = ('metodo', 'data_pagamento')
    search_fields = ('contrato__locatario__nome', 'contrato__locador__nome')