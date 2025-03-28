from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from .base_models import BaseModel
from django.db import models
from strava.enumerations import TipoEsporte

class Atividade(BaseModel):
    nome = models.CharField(
        max_length=100, validators=[MinLengthValidator(10)],
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",
    )

    observacoes = models.CharField(
        max_length=100, validators=[MinLengthValidator(10)],
        help_text="Observações",
        verbose_name="Opicional",
    )

    data = models.DateField(
        null=False, blank=False,
        help_text="Data do Exercício",
        verbose_name="Data"   
    )

    esporte = models.CharField(
        max_length=50, null=False, blank=False,
        choices=TipoEsporte,
        help_text="Tipos de Esporte",
        verbose_name="Esporte",
    )

    duracao = models.TimeField(
        null=False, blank=False,
        help_text="Tempo em exercício",
        verbose_name="Duração",
    )

    distancia = models.FloatField(
        null=False, blank=False,
        default=0,
        help_text="Distancia total",
        verbose_name="Distancia percorrida",
    )

    ritmo = models.TimeField(
        null=False, blank=False,
        help_text="Pace",
        verbose_name="Ritmo",
    )

    calorias = models.IntegerField(
        validators=[MinValueValidator(0)], default=0,
        null=False, blank=False,
        help_text="Calorias gastas no execício",
        verbose_name="Calorias",
    )

    elevacao = models.IntegerField(
        default=0,
        null=False, blank=False,
        help_text="--",
        verbose_name="Elevação",
    )

    def __str__(self):
        f"{self.nome} {self.observacoes} {self.data} {self.esporte} {self.duracao} {self.distancia} {self.ritmo} {self.calorias} {self.elevacao}"
    
    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"