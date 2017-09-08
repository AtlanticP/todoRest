
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from todoRest.views import ToDoListView, ToDoDetailView

urlpatterns = [
	url(r'^todo/api/(?P<pk>[0-9]+)/$', ToDoDetailView.as_view()),
    url(r'^todo/api/$', ToDoListView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='todo/index.html')),
]
