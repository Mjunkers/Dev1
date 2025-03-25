from django.contrib import admin
from aula.models import Person
from aula.models import Passport
from aula.models import Reporter
from aula.models import Article

admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Reporter)
admin.site.register(Article)
# Register your models here.
