from django.conf.urls import url
from alg.views import fibonacci

urlpatterns = [
    url(r'^fibonacci/(\d{1,2})/$', fibonacci),
]
