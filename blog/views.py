from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import LoginForm


def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def retrieve(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.views += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/view.html', context)


def reqister(request):
    return render(request, 'blog/register.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # if form.is_valid():
        #     return HttpResponseRedirect('/thanks/')
        print(form.cleaned_data)
    else:
        form = LoginForm()

    return render(request, 'blog/login.html', {'form': form})

