# Generated by Django 4.1.5 on 2023-01-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bandmodels", "0018_alter_bandresults_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bandresults",
            name="name",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
