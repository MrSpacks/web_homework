from django.urls import re_path
from ..views import topics

urlpatterns = [
    re_path(r'^$', topics, name='topics'),
    

]