from django.apps import AppConfig # type: ignore


class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'
