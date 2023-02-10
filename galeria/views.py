from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografias

def index(request):
    fotografias = Fotografias.objects.filter(publicada=True)
    dados = {
    1: {"nome":"Nebulosa de Carina",
        "legenda":"webbtelescope.org / NASA / James Webb"},
    2: {"nome":"Galáxia NGC 1079",
        "legenda":"nasa.org / NASA / Hubble"}
    }
    return render(request, 'galeria/index.html', {"cards": fotografias})
     

def imagem(request, foto_id):
    foto = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": foto})
