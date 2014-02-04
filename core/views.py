# coding: utf-8
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from core.models import Task, TaskForm
from django.utils import timezone
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def home(request):
        latest_task_list = Task.objects.all().order_by('-pub_date')
        paginator = Paginator(latest_task_list, 5)
        #Certificando de que o page request seja um inteiro, caso contrário irá para primeira pagina
        try:
                page = int(request.GET.get('page', '1'))	
        except ValueError:
                page = 1
        #Se o page request estiver fora da lista, irá para ultima pagina
        try:
                tasks = paginator.page(page)
        except (EmptyPage, InvalidPage):
                tasks = paginator.page(paginator.num_pages)
        
        date = Task(pub_date=timezone.now())
        if request.method == 'POST':
                form = TaskForm(request.POST, instance=date)
                if form.is_valid():
                        form.save()
        else:
                form = TaskForm(instance=date)
        return render_to_response("tasks.html",{'form':form,'tasks':tasks,}, context_instance=RequestContext(request))


def contato(request):
        return render_to_response("contato.html",{})
    
    
def delete_task(request,id):
    dead_task = get_object_or_404(Task, pk=id)
    if request.method=='POST':
	dead_task.delete()
	return HttpResponseRedirect("/")
    return render_to_response("delete_task.html", {"dead_task":dead_task},
			      context_instance=RequestContext(request))
