from django.shortcuts import render , redirect , get_object_or_404
# from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request,'app/hello.html',{'posts':posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'app/create_post.html',{'form':form})


def update_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'app/update_post.html',{'form':form,'post':post})



def delete_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request,'app/delete.html',{'post':post})