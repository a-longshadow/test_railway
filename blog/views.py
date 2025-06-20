from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return Post.objects.filter(published=True).select_related('author')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, 'Your post has been created successfully!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, 'Your post has been updated successfully!')
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your post has been deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added successfully!')
            return redirect('blog:post_detail', pk=post.pk, slug=post.slug)
    return redirect('blog:post_detail', pk=post.pk, slug=post.slug)


def home_view(request):
    recent_posts = Post.objects.filter(published=True).select_related('author')[:6]
    
    # Get statistics for the homepage
    total_posts = Post.objects.filter(published=True).count()
    total_users = User.objects.count()
    total_comments = Comment.objects.filter(active=True).count()
    
    context = {
        'recent_posts': recent_posts,
        'total_posts': total_posts,
        'total_users': total_users,
        'total_comments': total_comments,
    }
    
    return render(request, 'blog/home.html', context)
