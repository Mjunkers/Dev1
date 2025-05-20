from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from .reporter import Reporter
from .revista import Magazine


class Article(BaseModel):
    titulo  = models.CharField(
        validators=[MinLengthValidator(10)], max_length=50,
        null=False, blank=False,
        help_text="Nome",
        verbose_name="Nome",
    )

    data_publicao = models.DateField(
        null=False, blank=False,
        help_text="Data de Publicação",
        verbose_name="Data de Publicação",
    )

    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    #magazine = models.ManyToManyField(Magazine)


    magazines = models.ManyToManyField(Magazine, null = True, blank=True, through="Publication", through_fields=("article", "magazine"))

