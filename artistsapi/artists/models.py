from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256)


class Album(models.Model):
    title = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, models.CASCADE)


class Track(models.Model):
    name = models.CharField(max_length=256)
    album = models.ForeignKey(Album, models.CASCADE)
    milliseconds = models.IntegerField()
