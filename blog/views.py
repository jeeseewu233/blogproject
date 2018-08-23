from django.shortcuts import render, get_object_or_404
from . import models
import markdown


def index(request):
    post_list = models.Post.objects.all().order_by('-created_time')
    context = {
        "post_list": post_list,
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.fenced_code',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    comment_list = post.comments_set.filter(post=post).order_by("-created_time")
    context = {
        "post": post,
        "comment_list": comment_list
    }
    return render(request, "blog/detail.html", context)


def archives(request, year, month):
    post_list = models.Post.objects.filter(created_time__year=year,
                                           created_time__month=month).order_by("-created_time")
    context = {
        "post_list": post_list,
    }
    return render(request, 'blog/index.html', context)


def category(request, category_id):
    category_name = models.Category.objects.get(pk=category_id)
    post_list = models.Post.objects.filter(category__name=category_name).order_by("-created_time")
    context = {
        "post_list": post_list,
    }
    return render(request, 'blog/index.html', context)
