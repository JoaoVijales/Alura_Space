from django.db import models
from datetime import datetime

class Fotografias(models.Model):
    OPCAO_CATEGORIA =[
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField( null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=False)
    categoria = models.CharField(max_length=100, choices=OPCAO_CATEGORIA, default='')
    publicada = models.BooleanField(default=False)
    data_foto = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self) -> str:
        return f"fotografia [nome={self.nome}]"