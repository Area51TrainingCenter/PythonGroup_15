from django.http import HttpResponse
import datetime


def root(request):
    # assert False  # Sirve para romper el flujo
    return HttpResponse('Area 51 Training Center')


def hello(request):
    return HttpResponse('Hola, estamos en TrialApp')


def hello_name(request, name):
    message = '''
        Hola {}, estás en TrialApp
    '''.format(name)
    return HttpResponse(message)


def hello_age(request, age):
    message = '''
            Hola, tu edad es {}.<br/> 
        '''.format(age)
    if int(age) > 17:
        message += 'Eres mayor de edad.'
    else:
        message += 'Eres menor de edad.'
    return HttpResponse(message)
