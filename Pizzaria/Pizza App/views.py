from django.shortcuts import render
from .models import Topic
def index(request):
    '''pagina inicial'''
    return render(request, 'pizza/index.html')


def topics(request):
    '''mostra as coisas'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'pizza/topics.html',context)

     