# Generated by Django 4.2.3 on 2023-07-29 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0028_alter_comment_approved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="approved",
        ),
        migrations.AddField(
            model_name="comment",
            name="like",
            field=models.IntegerField(default=2),
        ),
    ]
