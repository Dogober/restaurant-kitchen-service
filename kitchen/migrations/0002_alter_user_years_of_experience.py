# Generated by Django 5.1.5 on 2025-02-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="years_of_experience",
            field=models.IntegerField(null=True),
        ),
    ]
