from django.contrib.auth import get_user_model
from django.db.models import Sum, Q
from django.http import JsonResponse
from django.db.models import Count
from blog.models import Comment, Post, Topics

User = get_user_model()



def question_1_return_active_users():
    """
    Return the results of a query which returns a list of all
    active users in the database.
    """
        active_users = User.objects.filter(is_active=True)
        all_active_users = list(active_users)
        for active_users in all_active_users:
            print(active_users)
    """
    The answer should list all these
    [ < User: atifnadeem >, < User: Mark >, < User: Mike >, < User: Travis >]
    """
question_1_return_active_users()

    def question_2_return_regular_users():
    """
    Return the results of a query which returns a list of users that
    are *not* staff and *not* superusers
    """
        nstaff_nsuperuser = User.objects.filter(is_staff=False, is_superuser=False)
        list_nstaff_nsuperuser = list(nstaff_nsuperuser)
        for no_staff_no_superuser in list_nstaff_nsuperuser:
            print(no_staff_no_superuser)
    """
    The output should be like this
    
      [ < User: Mark >, < User: Mike >, < User: Travis >]
    """

question_2_return_regular_users()

    def question_3_return_all_posts_for_user(user):

    """
    Return all the Posts authored by the user provided. Posts should
    be returned in reverse chronological order from when they
    were created.
    """
        posts = Post.objects.filter(author_id=2)
        all_posts_by_user = list(posts)
        print(all_posts_by_user)

question_3_return_all_posts_for_user(author_id=2)

    """
    The output should be like this
    [<Post: The Power of Local SEO Keyword Research for Boosting Business Visibility>, 
    <Post: Understanding the Role of Meta Descriptions in SEO>, 
    <Post: Local SEO: Boost Your Business with Optimized Online Presence>]

    """


def question_4_return_all_posts_ordered_by_title():

    """
    Return all Post objects, ordered by their title.
    """
    posts = Post.objects.order_by('title')
    ordered_by_title = list(posts)
    print(ordered_by_title)

question_4_return_all_posts_ordered_by_title()

    """
    [<Post: Canonical URL and Its Role in Handling Duplicate Content>, <Post: Harness the Power of Local SEO Marketing to Reach Your Target Audience>, <Post: Local SEO: Boost Your Business with Optimized Online Presence>, <Post: Masteri
ng Off-Page SEO Strategies for Search Visibility and Authority>, <Post: SEO: Your Guide to Boosting Organic Traffic and Visibility>, <Post: Technical SEO: Optimizing Websites for Search Engines and Beyond>, <Post: The Impact of Tech
nical SEO on Google Ranking and Website Performance>, <Post: The Power of Local SEO Keyword Research for Boosting Business Visibility>, <Post: Understanding the Role of Meta Descriptions in SEO>, <Post: Understanding the Types of Keywords Based on User Search Intent in SEO>]

    """

def question_5_return_all_post_comments(post):
    """
    Return all the comments made for the post provided in order
    of last created.
    """

    post = Post.objects.get(id=6)
    comments = post.comments.order_by('created')
    print(comments)

question_5_return_all_post_comments(post)

    """
    This is the answer I got
    <QuerySet [<Comment: Comment object (3)>]>

    """
def question_6_return_the_post_with_the_most_comments():
    """
    Return the Post object containing the most comments in
    the database. Do not concern yourself with approval status;
    return the object which has generated the most activity.
    """
    post = Post.objects.all()
    most_comments = post.annotate(num_comments=Count('comments')).order_by('-comments')
    print(most_comments)

question_6_return_the_post_with_the_most_comments()


def question_7_create_a_comment(post):
    """
    Create and return a comment for the post object provided.
    """
    comment = Comment.objects.create(post_id=6, user_name="Michael", email="michael@mik.net", text="I really like this post")
    comment_data = {

        'comment_user_name': comment.username,
        'comment_email': comment.email,
        'comment_text': comment.text,
        'post_title': comment.post.title,
    }

    return JsonResponse(comment_data)

question_7_create_a_comment(post_id=6)

def question_8_set_approved_to_false(comment):
    """
    Update the comment record provided and set approved=False
    """
    """
    I couldn't succeed in getting this done. I am having issue with BooleanField.
    """

def question_9_delete_post_and_all_related_comments(post):
    """
    Delete the post object provided, and all related comments.
    """

    post = Post.objects.get(id=9)
    post.delete()
    """
    My outcome:
    (3, {'blog.Post_topics': 1, 'blog.Comment': 1, 'blog.Post': 1})

    """
question_9_delete_post_and_all_related_comments(post)