from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Q, Count
from blog.models import Post, Topic, Comment
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .forms import ContestantSubmissionForm, CommentForm
from django.urls import reverse
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.db.models import F


class PostListView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"
    def get_queryset(self):
        pub_posts =  super().get_queryset()
        data = pub_posts.filter(status="PUBLISHED").distinct()
        return data
class PostDetailView(DetailView):
    template_name = "blog/single-post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_topics"] = self.object.topics.all()
        context["comment_form"] = CommentForm()
        context["comments"] = self.object.comments.all()
        return context
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        context = {

            "post": post,
            "post_topics": post.topics.all(),
            "comment_form": comment_form


        }
        return render(request, "blog/single-post.html", context)

class TopicListView(ListView):
    template_name = "blog/topic.html"
    model = Topic
    context_object_name = "blog_topics"

class TopicDetailView(DetailView):
    template_name = "blog/single_topic.html"
    model = Topic
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = Post.objects.filter(topics=self.object)[:5]
        return context
def submit_image(request):
    if request.method == "POST":
        form = ContestantSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "blog/submission_success.html")
    else:
        form = ContestantSubmissionForm()
    return render(request, "blog/photo_submission.html", {'form': form})



def like_comments(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.likes = F('likes') + 1
    comment.save()
    return JsonResponse({'likes': comment.likes})

def dislike_comments(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.dislikes = F('dislikes') + 1
    comment.save()
    return JsonResponse({'dislikes': comment.dislikes})