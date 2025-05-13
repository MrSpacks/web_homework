from django.db import models
from django.contrib.auth.models import User


TOPIC_THEME_CHOICES = [
    ('1', 'Comics'),
    ('2', 'Movie'),
    ('3', 'TV'),
    ('4', 'Anime'),
    ('5', 'Book'),
    ('6', 'Music'),
    ('7', 'Game'),
    ('8', 'Other'),
]
class Topic(models.Model):
    """
    Model representing a topic.
    """
    name = models.CharField(max_length=100)
    theme = models.CharField( max_length=1, choices=TOPIC_THEME_CHOICES, default='8')
    сreated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Article(models.Model):
    """
    Model representing an article.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    topics = models.ManyToManyField(Topic, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    """
    Model representing a comment on an article.
    """
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return f"Comment by {self.by_user.username} on {self.article.title}"
    
User.add_to_class('subscribed_topics', models.ManyToManyField(Topic, blank=True))