from django.urls import path, re_path
from . import views

app_name = 'dozeros'

urlpatterns = [
        #pagina inicial 
        re_path(r'^$', views.index, name='index'),
        
        #todos os assuntos
        re_path(r'^topics/$', views.topics, name='topics'),
        
        #assunto unico
        re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        
        #novos assuntos
        re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
        
        #adicionar nova entrada
        re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,
        name='new_entry'),
        
        #editar entradas
        re_path(r'êdit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name = 'edit_entry')
]