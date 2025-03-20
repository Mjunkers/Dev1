from django.contrib import admin
from strava.models import Perfil
from strava.models import Clube
from strava.models import Equipamento
from strava.models import Atividade

admin.site.register(Perfil)
admin.site.register(Clube)
admin.site.register(Equipamento)
admin.site.register(Atividade)
# Register your models here.
