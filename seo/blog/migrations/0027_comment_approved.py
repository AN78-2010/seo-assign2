# Generated by Django 4.2.3 on 2023-07-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0026_remove_comment_approved"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]
