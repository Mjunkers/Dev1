from django.db import models
from .desafio import Desafio


class DesafioTempo(Desafio):
    meta_duracao=models.TimeField(
        null=False, blank=False,
        help_text="Tempo em exercício",
        verbose_name="Duração",
    )


    class Meta:
        verbose_name = "Desafio de Tempo"
        verbose_name_plural = "Desafios de Tempo"
        