from django.shortcuts import render, get_object_or_404
from . import models
from blog.models import Post


# Create your views here.
def post_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    name = request.POST['name']
    email = request.POST['email']
    url = request.POST['url']
    text = request.POST['comment']
    models.Comments.objects.create(name=name, email=email, url=url, text=text, post=post)
    comment_list = post.comments_set.filter(post=post).order_by("-created_time")
    context = {
        "post": post,
        "comment_list":comment_list
    }
    return render(request,"blog/detail.html",context)
