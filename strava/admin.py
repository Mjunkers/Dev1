from django.contrib import admin
from strava.models import Perfil
from strava.models import Clube
from strava.models import Equipamento
from strava.models import Atividade
from strava.models import Record
from strava.models import DesafioTempo

admin.site.register(Perfil)
admin.site.register(Clube)
admin.site.register(Equipamento)
admin.site.register(Atividade)
admin.site.register(Record)
admin.site.register(DesafioTempo)
# Register your models here.
