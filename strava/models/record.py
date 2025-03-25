from .base_models import BaseModel
from django.db import models
from strava.enumerations import TipoEsporte
from strava.enumerations import TipoMarca
from django.core.validators import MinLengthValidator


class Record(BaseModel):
    nome = models.CharField(
        max_length=20, validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",
    )

    marca = models.CharField(
        max_length=15,
        null=False, blank=False,
        choices=TipoMarca,
        help_text="Tipo de Record",
        verbose_name="Record",
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

    ritmo = models.TimeField(
        null=False, blank=False,
        help_text="Pace",
        verbose_name="Ritmo",
    )

    def __str__(self):
        return f"{self.nome} {self.marca} {self.esporte} {self.duracao} {self.ritmo}"
    
    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Recordes"