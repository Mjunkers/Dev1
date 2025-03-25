from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from .article import Article


class Magazine(BaseModel):
    nome  = models.CharField(
        validators=[MinLengthValidator(10)], max_length=50,
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",
    )

    edition = models.IntegerField(
        null=False, blank=False,
        help_text="Edição",
        verbose_name="Edição",
    )