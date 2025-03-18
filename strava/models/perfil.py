from django.core.validators import MinValueValidator, MaxValueValidator
from .base_models import BaseModel
from django.db import models
from strava.enumerations import Genero

class Perfil(BaseModel):
    description = models.CharField(
        max_length=100, 
        null=False, blank=False,
        help_text="Insira seu nome.",
        verbose_name="Nome",
    )

    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True,
        help_text="Insira seu e-mail",
        verbose_name="E-mail",
        default="teste@gmail.com"
    )

    generos = models.CharField(
        max_length=10, null=False, blank=False,
        choices=Genero,
        help_text="Selecione seu genero",
        verbose_name="Genero"
    )

    CPF = models.IntegerField(
        validators=[MinValueValidator(11), MaxValueValidator(11)],
        help_text="Insira seu CPF",
        verbose_name="CPF",
    )
    senha = models.CharField(
        max_length=20,
        help_text="Insira sua senha",
        verbose_name="Senha",
    )