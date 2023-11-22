from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class User(AbstractUser):
    pass


class Todo(models.Model):
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    def get_description(self):
        return self.description

    @staticmethod
    def get_all_todos():
        return Todo.objects.all()
