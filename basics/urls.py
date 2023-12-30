from django.urls import path

from . import views

app_name = 'basics'

urlpatterns = [
    path('', views.index, name='all'),
    path(r'^(?P<todo_id>[0-9]+)/done/$', views.mark_done, name='done'),
    path(r'^(?P<todo_id>[0-9]+)/undone/$', views.mark_not_done, name='undone'),
]
