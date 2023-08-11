from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.db.models import Q, Count
from blog.models import Post, Topic
from django.utils import timezone
from django.db.models import F
from django.contrib.auth.models import User

def index(request):
    topics_with_posts = Topic.objects.all().annotate(post_count=Count("post")).order_by("-post_count")
    latest_posts = Post.objects.all().order_by("-published")[:3]
    users = User.objects.all()[:4]
    context = {
        "topics": topics_with_posts,
        "latest_posts": latest_posts,
        "users": users,
    }
    return render(request, "seo/index.html", context)


class AboutView(TemplateView):
    template_name = "seo/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()[:4]
        context["topics_with_posts"] = Topic.objects.all().annotate(post_count=Count("post")).order_by("-post_count")
        return context

