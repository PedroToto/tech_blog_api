# Generated by Django 5.1.4 on 2025-01-17 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_alter_profile_gender_alter_profile_phone_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="Profile_photo",
            new_name="profile_photo",
        ),
    ]
