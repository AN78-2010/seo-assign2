# Generated by Django 4.2.3 on 2023-07-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_comment_approved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="approved",
        ),
        migrations.AddField(
            model_name="comment",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]
