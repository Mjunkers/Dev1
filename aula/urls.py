from django.urls import path
import aula.views as views_funcoes
from .views import *
#from .views.exemplo import PersonListView

app_name = 'aula'

urlpatterns = [
    path('teste', views_funcoes.primeira_view, name="primeira_view"),
    path('classe/teste', PrimeiraView.as_view(), name ="primeira_view_classe"),
    path('classe/saudacao', views_funcoes.saudacao, name="saudacao"),
    
    path('person/function', views_funcoes.person_list, name="person_function_list"),
    path('person/classe', PersonListView.as_view(), name="person_classe_list"),
]