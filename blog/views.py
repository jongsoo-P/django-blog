from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post, Category
from .forms import PostForm


### Post
class Index(View):

    def get(self, request):
        posts = Post.objects.all()
        context = {
            "posts": posts,
        }
        return render(request, 'blog/post_list.html', context)
    
class DetailView(View):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {
            "post": post,
        }
        return render(request, 'blog/post_detail.html', context)
    

class Write(View):

    def get(self, request):
        categorys = Category.objects.all()
        context = {
            'categorys': categorys,
            "title": "Blog"
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)
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
    

class Update(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        categorys = Category.objects.all()
        context = {
            'post': post,
            'categorys': categorys,
        }
        
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():    
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.category = form.cleaned_data['category']
            post.save()
            return redirect('blog:list')
        categorys = Category.objects.all()
        context = {
            'form': form,
            'categorys': categorys,
        }
        return render(request, 'blog/post_edit.html', context)
    

class Delete(View):
    
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('blog:list')