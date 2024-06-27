from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("Você chegou ao partão da casa.")


def sala(request):
    return HttpResponse("Você chegou na sala. Sente-se no sofá!")


def quarto(request):
    return HttpResponse("Agora esta no quarto, pode deitar.")


def post_list(request):
    return render(request, 'blog/post_list.html', {})