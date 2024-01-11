# Generated by Django 5.0 on 2024-01-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email_token",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="is_email_verified",
        ),
        migrations.AlterField(
            model_name="profile",
            name="created_up",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="updated_up",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
