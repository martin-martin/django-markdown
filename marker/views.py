import markdown

from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    md = markdown.Markdown()
    post_objects = Post.objects.all()
    post_texts = [md.convert(t.content) for t in post_objects]
    return render(request, "marker/index.html", context={"posts": post_texts})
