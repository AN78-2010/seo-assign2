# Generated by Django 4.2.3 on 2023-07-29 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0023_alter_comment_checkbox"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="checkbox",
        ),
        migrations.AddField(
            model_name="comment",
            name="approved",
            field=models.BooleanField(
                choices=[(False, "Object is Bad"), (True, "Object is Good")],
                default=True,
            ),
        ),
    ]
