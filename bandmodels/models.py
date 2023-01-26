from django.db import models

# Create your models here.


class BandResults(models.Model):
    name = models.CharField(max_length=30, blank=True,
                            default="Ime ni bilo vnešeno:")
    dex_ocena = models.IntegerField(default=0)
