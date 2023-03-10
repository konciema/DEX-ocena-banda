# Generated by Django 4.1.5 on 2023-01-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bandmodels", "0006_alter_band_author_songs_alter_band_fb_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="band",
            name="ig",
            field=models.CharField(
                choices=[
                    (
                        "less than 1.500",
                        "Izvajalec ima manj kot 1500 sledilcev na Instagramu.",
                    ),
                    (
                        "less than 3.000",
                        "Izvajalec ima manj kot 3000 sledilcev na Instagramu.",
                    ),
                    (
                        "more than 3.000",
                        "Izvajalec ima več kot 3000 sledilcev na Instagramu.",
                    ),
                ],
                max_length=100,
            ),
        ),
    ]
