from django.utils.translation import gettext_lazy as _
from django.db import models

#OPCAO = "valor_armazenado_no_banco", _("nome_exibido")
class TipoEsporte(models.TextChoices):
    RUN = "Corrida", _("Corrida")
    TRAIL_RUN = "TRAIL", _("Trilha")
    BIKE = "BIKE", _("Treino de Bicicleta")
    WALK = "WALK", _("Caminhada")
    HIT = "HIT", _("Treinamento de Alta Intensidade")
    STRENGTH = "STRENGTH", _("Treino de Força")
    CARDIO = "CARDIO", _("Treino Aeróbico")
    SWIMMING = "SWIMMING", _("Natação")