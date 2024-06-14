from django.db import models
from apps.users.models import User

class Subject(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название предмета'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название теста")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    time_limit = models.PositiveIntegerField(blank=True, null=True, verbose_name="Время на тест (в минутах)")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tests_created', verbose_name="Создано пользователем")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tests', verbose_name="Предмет")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        
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


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='results', verbose_name='Тест')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results', verbose_name='Пользователь')
    score = models.FloatField(verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения')

    def __str__(self):
        return f'{self.user.username} - {self.test.title}'

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'
