from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from .models import Post, Category
from .forms import PostForm
import math


categorys = Category.objects.all()
### Post
class Index(View):

    def get(self, request):
        per_page = 10
        page = request.GET.get('page', '1')
        posts = Post.objects.order_by('-created_at')
        paginator = Paginator(posts, per_page)
        lastPage = math.ceil(paginator.count/per_page)
        if(int(page) > lastPage):
            page = '1'
        page_obj = paginator.get_page(page)
        range_start = (int(page)-1)//5*5+1
        page_range = range(range_start,range_start+5 if range_start+4 < lastPage else (lastPage+1 if lastPage > 1 else 2))
        context = {
            "title": "Blog",
            "posts": page_obj,
            "lastPage": lastPage,
            "pageRange": page_range,
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
            "title": "글쓰기"
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():    
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        categorys = Category.objects.all()
        context = {
            "title": "글쓰기",
            'form': form,
            'categorys': categorys,
        }
        return render(request, 'blog/post_form.html', context)
    

class Update(LoginRequiredMixin, View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        categorys = Category.objects.all()
        context = {
            "title": "글 수정",
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
            "title": "글 수정",
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
        per_page = 10
        page = request.GET.get('page', '1')
        tags = tag.split('&')
        FILTER = {}
        if tags[0]:
            FILTER["category"] = int(tags[0])
        if tags[1]:
            FILTER["title__contains"] = tags[1]
        posts = Post.objects.filter(**FILTER).order_by('-created_at')
        paginator = Paginator(posts, per_page)
        lastPage = math.ceil(paginator.count/per_page)
        if(int(page) > lastPage):
            page = '1'
        page_obj = paginator.get_page(page)
        range_start = (int(page)-1)//5*5+1
        page_range = range(range_start,range_start+5 if range_start+4 < lastPage else (lastPage+1 if lastPage > 1 else 2))
        context = {
            "title": "Blog",
            "posts": page_obj,
            "lastPage": math.ceil(page_obj.paginator.count/per_page),
            "pageRange": page_range,
            "categorys": categorys
        }
        return render(request, 'blog/post_list.html', context)