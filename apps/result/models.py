from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)
    responses = models.JSONField()

    class Meta:
        unique_together = ('test', 'user')
