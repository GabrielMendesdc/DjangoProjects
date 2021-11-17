''' define padrões de URL para aprendizados.'''
from django.urls import path, re_path
from . import views

app_name = 'aprendizado'

urlpatterns = [
    #pagina inicial
    path('', views.index, name='index'),
    #mostra os assuntos
    path('topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
