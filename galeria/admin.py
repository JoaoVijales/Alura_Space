from django.contrib import admin
from galeria.models import Fotografias

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page= 1

admin.site.register(Fotografias, ListandoFotografias)

