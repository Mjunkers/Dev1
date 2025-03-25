from .base_model import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator

class Person(BaseModel):
    nome = models.CharField(
        validators=[MinLengthValidator(10)], max_length=50,
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",

    )

    data_aniversario = models.DateField(
        null=False, blank=False,
        help_text="Data de Anivesário",
        verbose_name="Data de Aniversário",
        
    )

    cpf = models.CharField(
        validators=[MinLengthValidator(11)], max_length=11,
        null=False, blank=False,
        help_text="CPF",
        verbose_name="CPF",
    )

    def __str__(self):
        f"{self.nome}, {self.data_aniversario}, {self.cpf}"