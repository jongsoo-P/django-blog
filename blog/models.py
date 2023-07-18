from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # writer
    # category
    # 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True,default='Null')


class Category(models.Model):
    name = models.CharField(max_length=10)