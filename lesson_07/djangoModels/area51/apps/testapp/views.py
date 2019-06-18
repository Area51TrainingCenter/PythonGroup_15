from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from .models import Developer, Company, Software

import datetime


def root(request):
    # assert False  # Sirve para romper el flujo
    return HttpResponse('Area 51 Training Center')


def hello(request):
    return HttpResponse('Hello World!')


def current_time(request):
    print(dir(request))  # Muestra en consola
    now = datetime.datetime.now()

    html = '''
    <html>
        <body>
            <h1>TEST: Hora Actual</h1>
            <h3>{}</h3>
        </body>
    </html>
    '''.format(now)

    return HttpResponse(html)


def time_ahead(request, ahead):
    now = datetime.datetime.now()
    time = now + datetime.timedelta(hours=int(ahead))
    html = '''
    <html>
        <body>
            <h1>TEST: Agregar {} hora(s)</h1>
            <h3>{}</h3>
        </body>
    </html>
    '''.format(ahead, time)
    return HttpResponse(html)


def create_dev(request, username):
    # lastname = username[::-1]
    lastname = username.upper()[:4]
    email = '{}@area51.pe'.format(username)
    # dev = Developer.objects.create(name=username, lastname=lastname, email=email)
    dev = Developer(name=username, lastname=lastname, email=email)
    dev.save()
    return HttpResponse('Created Developer')


def delete_dev(request, id):
    # delete from developer where id = id
    deleted = Developer.objects.filter(id=id).delete()
    return HttpResponse(deleted)


def update_dev(request, id):
    # select * from developer where id = id
    dev = Developer.objects.get(id=id)
    dev.email = 'changed@gmail.com'
    dev.save()
    return HttpResponse('Updated Developer')


def get_dev(request, id):
    # dev = Developer.objects.get(id=id)
    # s = "{} {}".format(dev.name, dev.lastname)
    # return HttpResponse(s)
    devs = Developer.objects.filter(id=id)
    if devs:
        s = "{} {}".format(devs[0].name, devs[0].lastname)
    else:
        s = "No existe el developer con id: {}".format(id)
    return HttpResponse(s)


def filter_devs(request, name):
    # select * from developer where name = name
    devs = Developer.objects.filter(name=name)
    s = ""
    for dev in devs:
        s += "{} {}<br>".format(dev.name, dev.lastname)
    return HttpResponse(s)


def filter_devs_for_domain(request, domain):
    # select * from developer where email like %domain%
    devs = Developer.objects.filter(email__contains=domain)
    s = ""
    for dev in devs:
        s += "{} {}<br>".format(dev.name, dev.email)
    return HttpResponse(s)


def devs(request):
    devs = Developer.objects.all()  # select * from developer
    s = '<strong># id  name  lastName Email</strong><br>'
    for i, dev in enumerate(devs):
        s += '<strong>#{}</strong> {} {} {} - {}<br>'.format(i, dev.id, dev.name, dev.lastname, dev.email)
    return HttpResponse(s)


def devs_template(request):
    devs = Developer.objects.all()
    context = {'devs': devs}
    return render(request, 'test/testapp.html', context)

