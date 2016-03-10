from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name="likes")
    answers = models.ManyToManyField(Answer)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    question = models.OneToOneField(Question)
    author = models.OneToOneField(User)
