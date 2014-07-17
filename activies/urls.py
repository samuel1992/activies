from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^contato/$', 'core.views.contato', name='contato'),
    url(r'^delete/(?P<id>\d+)/$', 'core.views.delete_task', name='delete_task'),
    url(r'^done/(?P<id>\d+)/$', 'core.views.task_done', name='task_done'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()

