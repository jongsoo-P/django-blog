from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, default='Null')

    def __str__(self) -> str:
        return f'num:{str(self.pk)}, title:{self.title}'


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name