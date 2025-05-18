from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'topics']  # добавь topic, если он есть в модели
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }