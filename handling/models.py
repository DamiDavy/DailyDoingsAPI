from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "month": self.month,
            "day": self.day,
            "user": self.user.username,
        }

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")
    creation_date = models.DateField(auto_now=False, auto_now_add=True)
