from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользаватель'
        verbose_name_plural = 'Пользаватели'
        
class Employee(models.Model):
    class EmployeePostionChoice(models.TextChoices):
        ADMINISTRATOR = 'Администратор', 'Администратор'
        DIRECTOR = 'Завуч', 'Завуч'
        TEACHER = 'Учитель', 'Учитель'
        STUDENT = 'Студент', 'Студент'
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL,
        related_name="user_employee",
        verbose_name="Аккаунт пользователя",
        blank=True, null=True, unique=True
    )
    first_name = models.CharField(
        max_length=255, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255, verbose_name="Фамилия",
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=100, verbose_name="Номер телефона",
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        blank=True, null=True
    )
    employee_position = models.CharField(
        max_length=100, verbose_name="Должность", 
        choices=EmployeePostionChoice.choices,
        default=EmployeePostionChoice.STUDENT
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.employee_position}"
    

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"