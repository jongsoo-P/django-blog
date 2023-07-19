from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Category
from .forms import PostForm


categorys = Category.objects.all()
### Post
class Index(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        context = {
            "posts": posts,
            "categorys": categorys,
        }
        return render(request, 'blog/post_list.html', context)
    
class DetailView(View):

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return render(request, 'blog/post_404.html')
        # except:
        #     return redirect('blog:list')
        context = {
            "post": post,
        }
        return render(request, 'blog/post_detail.html', context)
    

class Write(LoginRequiredMixin, View):

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
    

class Update(LoginRequiredMixin, View):

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
    

class Search(View):

    def get(self, request, tag):
        tags = tag.split('&')
        FILTER = {}
        if tags[0]:
            FILTER["category"] = int(tags[0])
        if tags[1]:
            FILTER["title__contains"] = tags[1]
        posts = Post.objects.filter(**FILTER).order_by('-created_at')
        context = {
            "posts": posts,
            "categorys": categorys
        }
        return render(request, 'blog/post_list.html', context)