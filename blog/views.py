from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Category
from .forms import PostForm


### Post
class Index(View):

    def get(self,request):
        posts = Post.objects.all()
        context = {
            "posts": posts,
        }
        return render(request, 'blog/post_list.html', context)
    
class DetailView(View):

    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        context = {
            "post": post,
        }
        return render(request, 'blog/post_detail.html', context)
    

class Write(View):

    def get(self,request):
        form = PostForm()
        categorys = Category.objects.all()
        context = {
            'form': form,
            'categorys': categorys,
            "title": "Blog"
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self,request):
        form = PostForm(request.POST)
        print(form)
        print(request.POST)
        if form.is_valid():
            
            post = form.save(commit=False)
            # post.writer = request.user
            post.save()
            return redirect('blog:list')
        categorys = Category.objects.all()
        context = {
            'form': form,
            'categorys': categorys,
        }
        
        return render(request, 'blog/post_form.html', context)
        
