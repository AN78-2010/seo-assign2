from django.contrib import admin

from . models import Post, Topic, Comment

class TopicAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    list_filter = (

        "name",
    )

    prepopulated_fields = {"slug": ("name",)}

class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "user_name",
        "post",
        "email",
        "text",

    )
    search_fields = (
        "user_name",
        "email",
        "text",
    )
    readonly_fields = (
        "user_name",
        "email",
        "text",
    )
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0 # Number of empty comment forms to display

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = (
        "title",
        "created",
        "updated",

    )
    search_fields = (
        "topics__name",
        "author__username",
        "author__first_name",
        "author__last_name",
        "title",

    )
    list_filter = (
        "status",
        "topics",
    )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)


