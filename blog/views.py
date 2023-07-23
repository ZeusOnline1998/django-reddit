from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.
class Index(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment with the current user as the author and link it to the post
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)

    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})