from django.contrib import admin
from .models import Topic, Article, Comment

# Регистрируем модель Topic
admin.site.register(Topic)

# Регистрируем модель Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    filter_horizontal = ('topics',)  # Для отображения виджета M2M
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at', 'topics')

admin.site.register(Article, ArticleAdmin)

# Регистрируем модель Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'by_user', 'article', 'created_at')
    list_filter = ('by_user', 'article', 'created_at')
    search_fields = ('text', 'by_user__username', 'article__title')  # Поиск по связанным полям

admin.site.register(Comment, CommentAdmin)