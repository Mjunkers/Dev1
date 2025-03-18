from django.contrib import admin
from my_app.models import  Tag, Example
from strava.models import Perfil

admin.site.register(Tag)
admin.site.register(Example)
admin.site.register(Perfil)
# Register your models here.
