# Generated by Django 4.2.3 on 2023-07-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_comment_email_alter_comment_text_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="approved",
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.TextField(max_length=400, null=True),
        ),
    ]
