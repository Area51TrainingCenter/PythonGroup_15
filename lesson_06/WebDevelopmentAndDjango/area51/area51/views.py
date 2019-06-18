from django.http import HttpResponse


def hello_view(request):
    return HttpResponse("¡Hola Mundo!")


def home(request):
    return HttpResponse("Welcome")
