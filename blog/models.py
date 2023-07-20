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
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, default='Null')

    def __str__(self) -> str:
        return f'num:{str(self.pk)}, title:{self.title} {self.writer.email}'


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    

class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class Photo(models.Model):
    filePath = models.CharField(max_length=255)
    originName = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'post: {self.post.pk}, {self.post.title}, fileName: {self.originName}'
    

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.IntegerField(null=False, default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'post: {self.post.pk}, {self.post.title}, fileName: {self.writer.email}'