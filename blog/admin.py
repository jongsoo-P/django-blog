from django.contrib import admin
from .models import Post, Category # model 임포트

admin.site.register(Post)
admin.site.register(Category)