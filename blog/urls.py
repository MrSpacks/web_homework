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
