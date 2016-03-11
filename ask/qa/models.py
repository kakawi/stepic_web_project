from django.utils import timezone
from django.core.urlresolvers import reverse

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True)
    likes = models.ManyToManyField(User, related_name="likes")

    def get_url(self):
        return reverse('question_id', kwargs={'id':self.pk})

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    added_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True)
