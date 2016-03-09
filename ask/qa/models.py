from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.OneToOneField(Question)
    author = models.OneToOneField(User)


# Question - вопрос
# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"
#
# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа