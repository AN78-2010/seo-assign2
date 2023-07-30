# Generated by Django 4.2.3 on 2023-07-29 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_alter_comment_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="status",
        ),
        migrations.AddField(
            model_name="comment",
            name="approved",
            field=models.BooleanField(default=True),
        ),
    ]
