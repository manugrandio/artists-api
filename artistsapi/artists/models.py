from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class AlbumManager(models.Manager):
    def get_detailed_albums(self):
        return (
            self.prefetch_related("artist", "tracks")
            .annotate(
                track_count=models.Count("tracks"),
                total_duration=models.Sum("tracks__milliseconds"),
                min_duration=models.Min("tracks__milliseconds"),
                max_duration=models.Max("tracks__milliseconds"),
            )
            .order_by("id")
        )


class Album(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, models.CASCADE, related_name="albums")

    objects = AlbumManager()


class Track(models.Model):
    name = models.CharField(max_length=256)
    album = models.ForeignKey(Album, models.CASCADE, related_name="tracks")
    milliseconds = models.IntegerField()
