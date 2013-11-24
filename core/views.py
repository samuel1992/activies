# coding: utf-8
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response
from core.models import Task, TaskForm
from django.utils import timezone
from django.forms.models import modelform_factory

def home(request):
	latest_task_list = Task.objects.all().order_by('-pub_date')
	date = Task(pub_date=timezone.now())
	if request.method == 'POST':
		form = TaskForm(request.POST or None, instance=date)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = TaskForm(instance=date)
	return render_to_response("index.html",{'form':form, 'latest_task_list':latest_task_list}, context_instance=RequestContext(request))


def contato(request):
	return render_to_response("contato.html",{})