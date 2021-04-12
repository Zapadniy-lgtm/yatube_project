from django.shortcuts import render

from .models import Post

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest}) 


def index_wrong(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    render(request, "index.html", {"posts": latest})

# Хороший вариант: промежуточные переменные полезны
def index_ok(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    response = render(request, "index.html", {"posts": latest})
    return response

# Хороший вариант: без промежуточных переменных - короче
def index_ok_too(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest}) 


