# Generated by Django 5.0.3 on 2024-03-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]