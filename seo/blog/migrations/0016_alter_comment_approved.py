# Generated by Django 4.2.3 on 2023-07-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0015_remove_comment_status_comment_approved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]