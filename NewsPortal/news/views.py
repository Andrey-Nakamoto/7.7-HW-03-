from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import *
from .forms import *
from .models import *


class AuthorList(ListView):
    model = Author
    context_object_name = 'Author'

class PostsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class SearchPostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news_search.html'
    context_object_name = 'news_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'PS'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'
    success_url = reverse_lazy('news')


class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'
    success_url = reverse_lazy('news')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')