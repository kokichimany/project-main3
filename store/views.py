# store/views.py — обновлён полностью
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment, Post, PostComment, Category
from .forms import CommentForm, PostForm, PostCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Главная страница: список товаров
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# Страница с деталями товара + комментарии к товару
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = Comment.objects.filter(product=product).order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = CommentForm()
    return render(request, 'store/product_detail.html', {'product': product, 'comments': comments, 'form': form})

# Список постов
def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'store/post_list.html', {'posts': posts})

# Детали поста и комментарии к нему
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = PostComment.objects.filter(post=post).order_by('-created_at')
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostCommentForm()
    return render(request, 'store/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# Создание поста
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'store/post_form.html', {'form': form})

# Регистрация нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})
