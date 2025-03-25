from django.db import models
from django.core.validators import MinLengthValidator
from .base_model import BaseModel

class Reporter (BaseModel):
    name = models.CharField(
        validators=[MinLengthValidator(10)], max_length=50,
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",
    )
    
    email = models.EmailField(
        null=False, blank=False,
        help_text="E-mail",
        verbose_name="E-mail",
    )

    cpf = models.CharField(
        validators=[MinLengthValidator(11)], max_length=11,
        null=False, blank=False,
        help_text="CPF",
        verbose_name="CPF",
    )