from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.db.models import Q, Count
from blog.models import Post, Topic
from django.utils import timezone
from django.contrib.auth.models import User





class HomeView(TemplateView):
    template_name = "seo/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_posts = Post.objects.all().order_by("-published")[:3]
        context = {"latest_posts":latest_posts}
        return context


class AboutView(TemplateView):
    template_name = "seo/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        return context

def terms_and_conditions(request):
    return render(request, "seo/terms_and_conditions.html")