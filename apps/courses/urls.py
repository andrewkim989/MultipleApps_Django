from django.conf.urls import url
from . import views   

urlpatterns = [
    url(r'^$', views.courses),
    url(r'^create$', views.add_process),
    url(r'^(?P<num>\d+)/delete$', views.delete),
    url(r'^(?P<num>\d+)/delete_process$', views.delete_process),
    url(r'^(?P<num>\d+)$', views.course),
    url(r'^(?P<num>\d+)/add$', views.adduser)
]