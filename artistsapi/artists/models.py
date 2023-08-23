from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, models.CASCADE, related_name="albums")


class Track(models.Model):
    name = models.CharField(max_length=256)
    album = models.ForeignKey(Album, models.CASCADE, related_name="tracks")
    milliseconds = models.IntegerField()
