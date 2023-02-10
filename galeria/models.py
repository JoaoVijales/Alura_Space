from django.db import models

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
    foto = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCAO_CATEGORIA, default='')

    def __str__(self) -> str:
        return f"fotografia [nome={self.nome}]"