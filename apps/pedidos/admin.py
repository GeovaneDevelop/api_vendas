from django.contrib import admin

from .models import Pedidos


class BasePedidos(admin.ModelAdmin):
    
    list_display = ('client', 'criado', 'status')
    list_filter = ('client', 'status')
    search_fields = ('client', 'status')


admin.site.register(Pedidos, BasePedidos)
