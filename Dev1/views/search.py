from aula.models.person import Person
from django.views import View
from django.http import Http404 
from django.shortcuts import render

class SearchView(View):
    @staticmethod
    def get(request):
        try:
            resultados = {}
            query = request.GET.get('query')

            exemplos = Person.objects.find_by_nome(query)
            if len(exemplos) ==0:
                raise Http404('No person')
            resultados_exemplos=[]
            for exemplo in exemplos:
                url = ""#reverse_lazy("aula:exemplo_classe_read")
                resultados_exemplos.append((url, exemplo))
            resultados["Person"] = resultados_exemplos
            context = {
                'results': resultados,
                'query': query,
            }

        except:
            context = {
                'query': query
            }
        return render(request, 'search/results.html', context)