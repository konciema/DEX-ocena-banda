# Generated by Django 4.1.5 on 2023-01-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bandmodels", "0011_remove_band_attributes_band_attribute_band_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="band",
            name="name",
            field=models.CharField(default=None, max_length=255),
        ),
    ]
