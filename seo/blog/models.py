from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import QuerySet


from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)
    def draft(self):
        return self.filter(status=self.model.DRAFT)

    def get_authors(self):
        User = get_user_model()
        return User.objects.filter(blog_posts__in=self).distinct()




class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_post',
        null=False,

    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Draft',
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        null=False,
        unique_for_date='published',
    )
    topics = models.ManyToManyField(Topic)
    objects = PostQuerySet.as_manager()



    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField(max_length=400, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)





    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.text










