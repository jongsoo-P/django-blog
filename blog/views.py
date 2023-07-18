from django.shortcuts import render
from django.views import View
from .models import Post


### Post
class Index(View):

    def get(self,request):
        posts = Post.objects.all()
        context = {
            "posts": posts,
        }
        return render(request, 'blog/index.html', context)
    
class DetailView(View):

    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        context = {
            "post": post,
        }
        return render(request, 'blog/post_detail.html', context)
