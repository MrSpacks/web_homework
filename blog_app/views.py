# from django.shortcuts import render

from django.http import HttpResponse, HttpRequest


def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("main")


def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("my-feed")

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

def profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("profile")

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("register")
def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("set-password")
def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("login")
def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("logout")