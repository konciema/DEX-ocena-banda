# Generated by Django 4.1.5 on 2023-01-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bandmodels", "0013_delete_band"),
    ]

    operations = [
        migrations.CreateModel(
            name="BandResults",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("dex_ocena", models.IntegerField(max_length=20)),
            ],
        ),
    ]
