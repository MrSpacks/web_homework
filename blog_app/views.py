from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpRequest


def main(request):
    return render(request, 'index.html')

def my_feed(request: HttpRequest) -> HttpResponse:
    return render(request, 'my_feed.html')

def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'profile.html')

def article(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"article {article_id}")
def comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"comment {article_id}")
def update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"update {article_id}")
def delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"delete {article_id}")

def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse("create")

def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("topics")


def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("register")
def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("set-password")
def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("login")
def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("logout")

def subscribe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("subscribe")
def unsubscribe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("unsubscribe")

def topic_id(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"topic {topic_id}")

def articles_by_month(request, year, month):
    # Проверка на корректность месяца
    if month < 1 or month > 12:
        raise Http404("Неверный месяц")

    # Проверка на корректность года (например, от 1900 до текущего + 10)
    current_year = datetime.now().year
    if year < 1900 or year > current_year + 10:
        raise Http404("Неверный год")

    # Здесь нужно получить статьи по году и месяцу
    # Пример (если есть модель Article с полем created_at):
    # from .models import Article
    # articles = Article.objects.filter(created_at__year=year, created_at__month=month)

    # Пока просто вернём шаблон-заглушку
    context = {
        'year': year,
        'month': month,
        # 'articles': articles
    }
    return render(request, 'blog_app/articles_by_month.html', context)