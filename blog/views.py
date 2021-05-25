from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import LoginForm, RegisterForm, CommentForms, NewPostForm
from django.http import HttpResponseRedirect


def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def retrieve(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    post = get_object_or_404(Post, id=pk)
    post.views += 1
    post.save()
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            instance = Comment()
            instance.owner = request.user
            instance.post = post
            instance.text = form.cleaned_data['text']
            instance.save()
    else:
        form = CommentForms()

    comments = Comment.objects.filter(post=pk)

    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'blog/view.html', context)


def reqister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.last_name = form.cleaned_data['lastName']
            user.first_name = form.cleaned_data['firstName']
            user.save()
    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'blog/login.html', {'form': form})


def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    if request.GET.get('query') is None:
        return render(request, 'blog/search.html')

    res = Post.objects.filter(Q(title__icontains=request.GET.get('query')) |
                              Q(clipped_text__icontains=request.GET.get('query')) |
                              Q(text__icontains=request.GET.get('query')))
    return render(request, 'blog/search.html', {'result': res})



def add_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    fix_me = ""

    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.owner = request.user
            post.title = form.cleaned_data['title']
            post.clipped_text = form.cleaned_data['clipped_text']
            post.text = form.cleaned_data['text']
            post.save()
            fix_me = "Запись успешно добавлена"
    else:
        form = NewPostForm()

    return render(request, 'blog/add_post.html', {'form': form, 'msg': fix_me})


def user(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    user = get_object_or_404(User, id=pk)
    posts = Post.objects.filter(owner = pk)
    context = {
        'user':user,
        'posts':posts,
    }
    return render(request, 'blog/user.html', context)


def error_404(request,exception):
    return render(request, 'blog/404.html')
