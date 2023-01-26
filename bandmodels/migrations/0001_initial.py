# Generated by Django 4.1.5 on 2023-01-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Band",
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
                (
                    "price",
                    models.CharField(
                        choices=[
                            ("more than 3000", "Več kot 3000 evrov"),
                            ("less than 3000", "Manj kot 3000 evrov"),
                            ("less than 2000", "Manj kot 2000 evrov"),
                            ("less than 1000", "Manj kot 1000 evrov"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "yt",
                    models.CharField(
                        choices=[
                            ("less than 3.000.000", "Manj kot 3 milijone ogledov"),
                            ("less than 5.000.000", "Manj kot 5 milijonov ogledov"),
                            ("less than 10.000.000", "Manj kot 10 milijonov ogledov"),
                            ("more than 10.000.000", "Več kot 10 milijonov ogledov"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "spo",
                    models.CharField(
                        choices=[
                            ("less than 5000", "Manj kot 5000 mesečnih poslušalcev"),
                            ("less than 7000", "Manj kot 7000 mesečnih poslušalcev"),
                            ("less than 10000", "Manj kot 10.000 mesečnih poslušalcev"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "hits",
                    models.CharField(
                        choices=[
                            (
                                "0",
                                "Izvajalec nima nobenega hita (skladbe z več kot 10.000 poslušanji na YT.",
                            ),
                            ("1-5", "Izvajalec ima 1 do 5 hitov."),
                            ("6-9", "Izvajalec ima 6 do 9 hitov."),
                            ("10 or more", "Izvajalec ima 10 ali več hitov"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "fb",
                    models.CharField(
                        choices=[
                            ("less than 5000", "Less than 5000 followers on Facebook."),
                            (
                                "less than 10000",
                                "Less than 10000 followers on Facebook.",
                            ),
                            (
                                "more than 10000",
                                "More than 10000 followers on Facebook.",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "ig",
                    models.CharField(
                        choices=[
                            (
                                "less than 1000",
                                "Less than 1000 followers on Instagram.",
                            ),
                            (
                                "less than 5000",
                                "Less than 5000 followers on Instagram.",
                            ),
                            (
                                "more than 5.000",
                                "More than 5000 followers on Instagram.",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "author_songs",
                    models.CharField(
                        choices=[
                            ("less than 3", "Less than 3 authored songs."),
                            ("less than 10", "Less than 10 authored songs"),
                            ("more than 10", "More than 10 authored songs"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "last_concert",
                    models.CharField(
                        choices=[
                            (
                                "1 year ago",
                                "The artist had a concert in NM less than 1 year ago",
                            ),
                            (
                                "2 years ago",
                                "The artist had a concert in NM less than 2 years ago",
                            ),
                            (
                                "more than 2 years ago",
                                "The artist had a concert in NM more than 2 years ago",
                            ),
                            ("Never", "The artist has never preformed in Novo mesto"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
