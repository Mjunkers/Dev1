from .base_model import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator
from .person import Person

class Passport(BaseModel):
    numer = models.CharField(
        validators=[MinLengthValidator(5)], max_length=14,
        null=False, blank=False,
        help_text="Número do passaporte",
        verbose_name="Passport",
    )

    data_expedicao = models.DateField(
        null=False, blank=False,
        help_text="Data de expedição",
        verbose_name="Data emissão",
    )

    expiration_date = models.DateField(
        null=False, blank=False,
        help_text="Data de expiração",
        verbose_name="Data Vencimento",

    )

    owner = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)