# Generated by Django 5.1.4 on 2025-01-20 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("responses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="response",
            name="parent_response",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="responses.response",
            ),
        ),
    ]
