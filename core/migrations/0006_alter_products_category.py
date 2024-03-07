# Generated by Django 5.0.3 on 2024-03-07 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_alter_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="category",
                to="core.category",
            ),
        ),
    ]
