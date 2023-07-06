from django.db import models
from django.contrib import auth

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    descript = models.TextField()
    task_created_date = models.DateTimeField()
    deadline = models.DateTimeField()


    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = "жалобы"

    def __str__(self):
        return self.title

    def get_time_diff(self):
        return self.deadline - self.task_created_date <= 0




