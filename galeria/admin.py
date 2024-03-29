from django.contrib import admin

from galeria.models import Fotografias

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda","data_foto", "publicada",)
    list_display_links = ("id","nome",)
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10


admin.site.register(Fotografias, ListandoFotografias)

