# coding: utf-8
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django import forms

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class TaskForm(ModelForm):
	class Meta:
		model = Task
		exclude = ('pub_date',)