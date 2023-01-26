# Generated by Django 4.1.5 on 2023-01-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bandmodels", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="band",
            name="spo",
            field=models.CharField(
                choices=[
                    ("less than 5000", "Manj kot 5000 mesečnih poslušalcev"),
                    ("less than 7000", "Manj kot 7000 mesečnih poslušalcev"),
                    ("less than 10000", "Manj kot 10.000 mesečnih poslušalcev"),
                    ("more than 10000", "Več kot 10.000 mesečnih poslušalcev"),
                ],
                max_length=100,
            ),
        ),
    ]