from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpRequest
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def main(request):
    return render(request, 'index.html')
# вывод всех статей
def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'all_articles.html', {'articles': articles})
# вывод статей по автору
@login_required
def my_feed(request):
    user = request.user
    articles = Article.objects.filter(author=user).order_by('-created_at')
    return render(request, 'my_feed.html', {'articles': articles})

def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'profile.html')
# Редактирование статьи
@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('my_feed')
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'edit_article.html', {'form': form})
# Удаление статьи
@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    
    if request.method == 'POST':
        article.delete()
        return redirect('my_feed')
    
    return render(request, 'delete_article.html', {'article': article})
def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {'article': article})
def comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"comment {article_id}")
def update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"update {article_id}")
def delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"delete {article_id}")

# создание статьи
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # назначаем автора
            article.save()
            return redirect('my_feed')  # или другой путь
    else:
        form = ArticleForm()
    
    return render(request, 'create.html', {'form': form})

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