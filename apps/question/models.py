from django.db import models
from apps.users.models import Employee
from apps.tests.models import Subject
from django.db import models

class Subject(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название предмета')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Question(models.Model):
    class QuestionType(models.TextChoices):
        MULTIPLE_CHOICE = 'multiple_choice', 'Множественный выбор'
        SINGLE_CHOICE = 'single_choice', 'Единственный выбор'
        FREE_ANSWER = 'free_answer', 'Свободный ответ'

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    question_type = models.CharField(max_length=20, choices=QuestionType.choices, verbose_name='Тип вопроса')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return f'{self.question} - {self.answer}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
