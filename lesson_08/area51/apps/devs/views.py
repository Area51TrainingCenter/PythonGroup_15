from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from apps.devs.models import Developer
from apps.devs.forms import FormDeveloper


class GetDevView(TemplateView):

    template_name = 'test/dev-update-form.html'

    def get(self, request, *args, **kwargs):
        dev = Developer.objects.filter(id=int(args[0]))[0]
        form = FormDeveloper({
            'name': dev.name,
            'lastname': dev.lastname,
            'email': dev.email
        })
        return self.render_to_response({'form': form, 'id': dev.id})


class UpdateDevView(TemplateView):

    template_name = 'test/dev-update-form.html'

    def post(self, request, *args, **kwargs):
        form = FormDeveloper(request.POST)
        if not form.is_valid():
            return self.render_to_response({'form': form})
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        id = int(args[0])
        dev = Developer.objects.filter(id=id)[0]
        dev.name = name
        dev.lastname = lastname
        dev.email = email
        dev.save()
        return HttpResponseRedirect(reverse('thanks') + "?name=" + name)


class CreateDevView(TemplateView):

    template_name = 'test/dev-form.html'

    def get(self, request, *args, **kwargs):
        form = FormDeveloper()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = FormDeveloper(request.POST)
        if not form.is_valid():
            return self.render_to_response({'form': form})
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        Developer.objects.create(name=name, lastname=lastname, email=email)
        return HttpResponseRedirect(reverse('thanks') + "?name=" + name)


def create_dev(request):
    errors = []
    name = request.POST.get('name', '')
    lastname = request.POST.get('lastname', '')
    email = request.POST.get('email', '')
    if request.method == 'POST':
        if not name:
            errors.append('Por favor introduce un nombre.')
        if not lastname:
            errors.append('Por favor introduce un apellido.')
        if not email or '@' not in email:
            errors.append('Por favor introduce una dirección de email válida.')
        if not errors:
            Developer.objects.create(name=name, lastname=lastname, email=email)
            return HttpResponseRedirect('/devs/thanks/?name=' + name)
    return render(request, 'test/form-dev.html', {
        'errors': errors,
        'name': name,
        'lastname': lastname,
        'email': email,
    })


def thanks(request):
    name = request.GET.get('name', '')
    return render(request, 'test/thanks.html', {'name': name})
