# Generated by Django 4.1.5 on 2023-01-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bandmodels", "0015_alter_bandresults_dex_ocena_alter_bandresults_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bandresults",
            name="dex_ocena",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="bandresults",
            name="name",
            field=models.CharField(default="", max_length=30),
        ),
    ]
