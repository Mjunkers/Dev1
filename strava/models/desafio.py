from .base_models import BaseModel
from django.db import models
from strava.enumerations import TipoEsporte
from django.core.validators import MinLengthValidator


class Desafio(BaseModel):
    nome = models.CharField(
        max_length=50, validators=[MinLengthValidator(5)],
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",
    )

    data_inicio = models.DateField(
        null=False, blank=False,
        help_text="Data de Início",
        verbose_name="Data de Início",
    )

    esporte = models.CharField(
        null=False, blank=False,
        max_length=20,
        choices=TipoEsporte,
        help_text="Tipo de Esporte",
        verbose_name="Esporte",
    )

    visao_geral = models.TextField(
        null=False, blank=False,
        help_text="Resumo",
        verbose_name="Resumo do Desafio",
    )

    selo = models.CharField(
        null=False, blank=False,
        max_length=5,
        help_text="Selo",
        verbose_name="Selo",
    )

    def __str__(self):
        return f"{self.nome} {self.data_inicio} {self.esporte} {self.visao_geral} {self.selo}"
    
    class Meta:
        verbose_name = "Desafio"
        verbose_name_plural = "Desafios"
        abstract=True