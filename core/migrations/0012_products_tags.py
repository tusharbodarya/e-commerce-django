# Generated by Django 5.0.3 on 2024-03-08 12:29

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_products_expriry_products_mfd_products_stock_count"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
