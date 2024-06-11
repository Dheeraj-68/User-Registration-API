# Generated by Django 4.2 on 2024-05-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UserProfile", "0006_remove_profile_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="first_name",
            new_name="profile_first_name",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="last_name",
            new_name="profile_last_name",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="middle_name",
            new_name="profile_middle_name",
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(blank=True, max_length=45, null=True),
        ),
    ]
