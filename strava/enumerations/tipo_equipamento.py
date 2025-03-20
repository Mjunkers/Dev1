from django.utils.translation import gettext_lazy as _
from django.db import models

#OPCAO = "valor_armazenado_no_banco", _("nome_exibido")
class TipoEquipamento(models.TextChoices):
    TENIS = "TENIS", _("Tênis")
    BIKE = "BIKE", _("Bicicleta")
    SMART_DEVICE = "DEVICE", _("Dipositivo inteligente: Celular, relogio, pulseira ..")
    