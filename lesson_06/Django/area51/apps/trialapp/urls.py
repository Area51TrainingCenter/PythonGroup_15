from django.conf.urls import url
from apps.trialapp.views import root, hello, hello_name, hello_age

urlpatterns = [
    url(r'^$', root),
    url(r'^hello/$', hello),
    url(r'^hello/([a-z]{3,8})/$', hello_name),
    url(r'^hello/[a-z]{3,8}/([0-9]|[1-9]{1}[0-9]{1})/$', hello_age)
]
