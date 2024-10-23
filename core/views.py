from django.http import HttpResponse
from django.template import loader

from .models import Post, Tag


def index(request):
    blog_posts = Post.objects.order_by("-created_at")[:]
    tags_list = Tag.objects.order_by("name")[:]
    template = loader.get_template("blog/index.html")
    context = {
        "blog_posts": blog_posts,
        "tags_list": tags_list
    }
    return HttpResponse(template.render(context, request))