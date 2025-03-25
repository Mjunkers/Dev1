from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from .base_models import BaseModel
from django.db import models
from strava.enumerations import TipoEquipamento
from strava.enumerations import TipoEsporte


class Equipamento(BaseModel):
    nome = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",
    )

    marca = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Marca",
        verbose_name="Marca",
    )

    modelo = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Modelo",
        verbose_name="Modelo",
    )
    
    apelido = models.CharField(
        max_length=50, validators=[MinLengthValidator(2)],
        null=False, blank=False,
        help_text="Apelido",
        verbose_name="Apelido",
    )

    equipamento = models.CharField(
        max_length=50, null=False, blank=False,
        choices=TipoEquipamento,
        help_text="Tipos de Equipamento",
        verbose_name="Equipamento",
    ) 

    esporte = models.CharField(
        max_length=50, null=False, blank=False,
        choices=TipoEsporte,
        help_text="Tipos de Esporte",
        verbose_name="Esporte",
    )

    distancia_total = models.FloatField(
        null=False, blank=False,
        default=0,
        help_text="Distancia total",
        verbose_name="Distancia percorrida",
    )

    distancia_prevista = models.IntegerField(
        null=False, blank=False,
        default=400,
        help_text="Minimo Desejavél",
        verbose_name="Distancia Mínima",
    )

    peso = models.FloatField(
        null=False, blank=False,
        validators=[MinValueValidator(0)],
        help_text="Peso",
        verbose_name="Peso",
        
    )

    notas = models.TextField(
        null=False, blank=True,
        help_text="Notas",
        verbose_name="Notas",
    )

    def __str__(self):
        return f"{self.nome} {self.marca} {self.modelo} {self.apelido} {self.equipamento}"
    
    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"