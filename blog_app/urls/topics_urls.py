from django.urls import re_path
from ..views import topics, subscribe, unsubscribe, topic_id

urlpatterns = [
    re_path(r'^$', topics, name='topics'),
    re_path(r'^(?P<topic_id>\d+)/$', topic_id, name='topic_id'),
    re_path(r'^(?P<topic_id>\d+)/subscribe/$', subscribe, name='subscribe'),
    re_path(r'^(?P<topic_id>\d+)/unsubscribe/$', unsubscribe, name='unsubscribe'),
    

]
