''' define padrões url para pizza '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
               ]

