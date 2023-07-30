# Generated by Django 4.2.3 on 2023-07-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0018_alter_comment_approved_alter_comment_created_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="approved",
        ),
        migrations.AlterField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]