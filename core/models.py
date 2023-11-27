from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from simple_history.models import HistoricalRecords


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',max_length=100)
    description = models.TextField(verbose_name='Описание категории')
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории" 

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория',null=True)
    title = models.CharField(verbose_name='Вопрос', max_length=200)
    content = models.TextField(verbose_name='Текст вопроса' )
    created_at = models.DateTimeField(verbose_name='Дата создания вопроса',auto_now_add=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы" 

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name='Ответ')
    content = models.TextField(verbose_name='Текст ответа' )
    created_at = models.DateTimeField(verbose_name='Дата создания ответа',auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы" 

class QuestionRating(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name='Вопрос')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователь')
    rating = models.IntegerField(verbose_name='Рейтинг вопроса',validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(verbose_name='Дата рейтинга вопроса',auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Рейтинг вопроса"
        verbose_name_plural = "Рейтинг вопросов" 

class AnswerRating(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,verbose_name='Ответа')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователь')
    rating = models.IntegerField(verbose_name='Рейтинг ответа',validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(verbose_name='Дата рейтинга ответа',auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Рейтинг ответа"
        verbose_name_plural = "Рейтинг ответов" 
