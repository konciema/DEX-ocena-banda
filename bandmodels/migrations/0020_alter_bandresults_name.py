# Generated by Django 4.1.5 on 2023-01-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bandmodels", "0019_alter_bandresults_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bandresults",
            name="name",
            field=models.CharField(
                blank=True, default="Ime ni bilo vnešeno:", max_length=30
            ),
        ),
    ]
