from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from datetime import datetime

def primeira_view(request):
    mensagem = "Boa noite DEV 1"
    return HttpResponse (mensagem, status = 200)

class PrimeiraView(View):
    @staticmethod
    def get(request):
        mensagem = "Boa noite DEV 1"
        return HttpResponse(mensagem, status=200)

def saudacao(request):
    agora = datetime.now()
    mensagem = "Boa noite"
    if 12 > agora.hour -3 > 6:
        mensagem = "Bom dia"
    elif 0 < agora.hour -3 <=6:
        mensagem = "Boa madrugada"

    completo = f"<html><body><h1>{mensagem.capitalize()} visitante!" \
                f"<br />{agora}</h1></body></html>"

    mensagem += str(agora)
    #return HttpResponse(mensagem, status=200)
    return HttpResponse(completo)