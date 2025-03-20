from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator,URLValidator
from .base_models import BaseModel
from django.db import models
from strava.enumerations import TipoEsporte


class Clube(BaseModel):
    nome = models.CharField(
        null=False, blank=False,
        validators=[MinLengthValidator(3)], max_length=(100),
        help_text="Nome do Clube",
        verbose_name="Clube", 
    )

    local = models.CharField(
        null=False, blank=False,
        max_length=100, validators=[MinLengthValidator(3)],
        help_text="Cidade",
        verbose_name="Cidade",        
    )

    pais = models.CharField(
        null=False, blank=False,
        max_length=100, validators=[MinLengthValidator(3)],
        help_text="País",
        verbose_name="País",
        
    )

    biografia = models.TextField(
        null=False, blank=True,
        help_text="Biografia - Campo Opicional",
        verbose_name="Biografia",
    )
    
    site = models.URLField(
        null=False, blank=False,
        validators=[MinLengthValidator(15)],
        max_length=150,
        help_text="Página Web do Clube",
        verbose_name="Página do Clube",
        
    )

    esporte = models.CharField(
        max_length=50, null=False, blank=False,
        choices=TipoEsporte,
        help_text="Tipos de Esporte",
        verbose_name="Esporte",
    )

    def __str__(self):
        return f"{self.nome} {self.local} {self.pais} {self.esporte} {self.biografia} {self.site}"
    
    class Meta:
        verbose_name = "Clube"
        verbose_name_plural = "Clube"