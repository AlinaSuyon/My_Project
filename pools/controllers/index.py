from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'interests.html',{})


def contacts(request):
    return HttpResponse("My name is Alina")


def hobbies(request):
    return HttpResponse("My name is Alina")


def gallery(request):
    return HttpResponse("My name is Alina")


def main(request):
    return render(request, 'index.html', {})
