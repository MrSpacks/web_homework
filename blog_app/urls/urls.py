# app urls
from django.urls import re_path
from ..views import article, comment, update, delete

urlpatterns = [
    re_path(r'^/$', article, name='article'),
    re_path(r'^comment/$', comment, name='comment'),
    re_path(r'^update/$', update, name='update'),
    re_path(r'^delete/$', delete, name='delete'),

]