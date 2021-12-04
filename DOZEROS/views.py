from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    ''' pagina inicial do projeto'''
    return render(request, 'dozeros/index.html')
 
 
@login_required
def topics(request):
    '''mostra os assuntos'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'dozeros/topics.html', context)
    

@login_required    
def topic(request, topic_id):
    '''um assunto, varias entradas'''
    topic = Topic.objects.get(id=topic_id)
    #garante que o assunto seja só seu
    check_topic_owner(topic,request)
        
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'dozeros/topic.html', context)
    

@login_required    
def new_topic(request):
    '''novo assunto'''
    if request.method != 'POST':
        #sem dados, cria formulário
        form = TopicForm()
    else:
        #dados POST, procesa eles
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('dozeros:topics'))
    
    context = {'form': form}
    return render(request, 'dozeros/new_topic.html', context)
    
 
@login_required 
def new_entry(request, topic_id):
    '''adiciona uma nova entrada do assunto'''
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic,request)
    if request.method != 'POST':
        #nenhum dado, cria form em branco
        form = EntryForm()
    else:
        #processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid() and topic.owner == request.user:
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('dozeros:topic',
                                        args=[topic_id]))
        else:
            raise Http404
    context = {'topic': topic,'form': form}
    return render(request, 'dozeros/new_entry.html', context)
    
 
@login_required 
def edit_entry(request, entry_id):
    '''edita uma entrada existente'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic,request)
        
    if request.method != 'POST':
        #requisição inicial preenche com a entrada atual
        form = EntryForm(instance=entry)
        
    else:
        #dados POST, para processa-los
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dozeros:topic',
                                    args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form': form}
    return render(request, 'dozeros/edit_entry.html', context)
    
    
def check_topic_owner(topic,request):
    if topic.owner != request.user:
        raise Http404