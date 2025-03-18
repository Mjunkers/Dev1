from django.utils.translation import gettext_lazy as _
from django.db import models

class Status(models.TextChoices):
    MAN = "MAN", _("Homem")
    WOMAN = "WOMAN", _("Mulher")
    NON_BINARY = "N_BINARY", _("Não Binário")
    NOT_INFORMED = "N_INFORM" , _("Não informado")
    