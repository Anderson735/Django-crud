from django.conf.urls import url;
from tutoriales import views;

urlpatterns = [
    url(r'^api/tutoriales$', views.tutorial_lista),
    url(r'^api/tutoriales/(?P<pk>[0-9]+)$', views.tutorial_detalle),
    url(r'^api/tutoriales/publicados$', views.tutorial_list_publicado)
];