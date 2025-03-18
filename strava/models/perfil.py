from django.core.validators import MinValueValidator, MaxValueValidator
from .base_models import BaseModel
from django.db import models
from strava.enumerations import genero

class Perfil(BaseModel):
    description = models.CharField(
        max_length=100, 
        null=False, blank=False,
        help_text="Insira seu nome.",
        verbose_name="Nome",
    )