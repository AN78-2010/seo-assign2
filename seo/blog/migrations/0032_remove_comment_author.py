# Generated by Django 4.2.3 on 2023-07-30 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0031_remove_comment_user_comment_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="author",
        ),
    ]