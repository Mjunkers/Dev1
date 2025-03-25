from django.utils.translation import gettext_lazy as _
from django.db import models


#OPCAO = "valor_armazenado_no_banco", _("nome_exibido")
class TipoMarca(models.TextChoices):
    CEM_METROS = "100M", _("100 Metros")
    QUATROCENTOS_METROS = "400M", _("400 Metros")
    UM_KM = "1KM", _("1 Quilômetro")
    CINCO_KM = "5KM", _("5 Quilômetros")
    DEZ_KM = "10KM", _("10 Quilômetros")
    QUINZE_KM = "15KM", _("15 Quilômetros")
    VINTE_KM = "20KM", _("20 Quilômetros")
    MEIA_MARATONA = "MEIA MARATONA", _("Meia Maratona")
    TRINTA_KM = "30KM", _("30 Quilômetros")
    MARATONA = "MARATONA", _("Maratona")
    LONGA_DISTANCIA = "LONGA DISTANCIA", _("Maior distância")
    LOGA_DURACAO = "LONGA DURACAO", _("Maior duração")