from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    posts = Post.objects.filter(pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
    #new = [{'title': 'new', 'published_date': 'a_date', 'text': 'a_text'}]
    #return render(request, 'blog/post_list.html', {'posts': new})
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #message = 'posted'
            #return render(request, 'blog/post_edit.html', {'message': message})
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
