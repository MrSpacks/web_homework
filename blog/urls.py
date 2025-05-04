from django.contrib import admin 
from django.urls import path 
from blog_app.views import main, my_feed, create, profile ,register, set_password, login, logout, articles_by_month
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main), 
    path('my_feed/', my_feed),
    path('<int:article_id>/', include('blog_app.urls.urls')),
    path('create/', create, name='create'),
    path('topics/', include('blog_app.urls.topics_urls')),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('set-password/', set_password, name='set_password'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('<int:year>/<int:month>/', articles_by_month, name='articles_by_month'),

]
"""



/<int:year>/<int:month>/ - страница, на которой будут статьи созданные в конкретный месяц. В случае запроса не настоящей даты, должна быть ошибка.

Например:

/2022/10/ - все хорошо
/2059/12/ - тоже все хорошо, но статей нет
/123/10/ - ошибка
/123/14/ - ошибка
/2020/22/ - ошибка
"""