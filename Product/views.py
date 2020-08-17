from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def new(request):
    return render(request, 'Product/new.html')

def create(request):
    if request.method == "POST" :
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        Post.objects.create(title=title, content=content, image=image, user=user, price=price, stock=stock)
        return redirect('Product:main')

def main(request) :
    Product = Post.objects.all()
    return render(request, 'Product/main.html', {'Product':Product})

def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'Product/show.html', {'post':post})


def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.image = request.FILES.get('image')
        post.price = request.POST['price']
        post.stock = request.POST['stock']
        post.save()
        return redirect('Product:show', post.id)
    return render(request, 'Product/update.html', {"post":post})

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("Product:main")
