from django.conf.urls import url
from apps.devs import views


urlpatterns = [
    url(r'^create-dev/$', views.create_dev),
    url(r'^dev-create/$', views.CreateDevView.as_view()),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^dev-get/(\d)$', views.GetDevView.as_view()),
    url(r'^dev-update/(\d)$', views.UpdateDevView.as_view())
]
