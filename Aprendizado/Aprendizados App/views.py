from django.shortcuts import render
from .models import Topic

def index(request):
    '''pagina inicial'''
    return render(request, 'aprendizados/index.html')


def topics(request):
    ''' mostra tudo '''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'aprendizados/topics.html', context)

    
def topic(request, topic_id):
    '''Mostra um único assunto e todas as suas entradas.'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'aprendizados/topic.html', context)
