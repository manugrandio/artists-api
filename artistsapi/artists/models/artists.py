from django.db import models


class Albums(models.Model):
    albumid = models.AutoField(
        db_column="AlbumId", primary_key=True
    )  # Field name made lowercase.
    title = models.TextField(
        db_column="Title"
    )  # Field name made lowercase. This field type is a guess.
    artistid = models.ForeignKey(
        "Artists", models.CASCADE, db_column="ArtistId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "albums"


class Artists(models.Model):
    artistid = models.AutoField(
        db_column="ArtistId", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = "artists"


class Genres(models.Model):
    genreid = models.AutoField(
        db_column="GenreId", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = "genres"


class MediaTypes(models.Model):
    mediatypeid = models.AutoField(
        db_column="MediaTypeId", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = "media_types"


class PlaylistTrack(models.Model):
    playlistid = models.OneToOneField(
        "Playlists", models.CASCADE, db_column="PlaylistId", primary_key=True
    )  # Field name made lowercase. The composite primary key (PlaylistId, TrackId) found, that is not supported. The first column is selected.
    trackid = models.ForeignKey(
        "Tracks", models.CASCADE, db_column="TrackId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "playlist_track"


class Playlists(models.Model):
    playlistid = models.AutoField(
        db_column="PlaylistId", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = "playlists"


class Tracks(models.Model):
    trackid = models.AutoField(
        db_column="TrackId", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name"
    )  # Field name made lowercase. This field type is a guess.
    albumid = models.ForeignKey(
        Albums, models.CASCADE, db_column="AlbumId", blank=True, null=True
    )  # Field name made lowercase.
    mediatypeid = models.ForeignKey(
        MediaTypes, models.DO_NOTHING, db_column="MediaTypeId"
    )  # Field name made lowercase.
    genreid = models.ForeignKey(
        Genres, models.DO_NOTHING, db_column="GenreId", blank=True, null=True
    )  # Field name made lowercase.
    composer = models.TextField(
        db_column="Composer", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    milliseconds = models.IntegerField(
        db_column="Milliseconds"
    )  # Field name made lowercase.
    bytes = models.IntegerField(
        db_column="Bytes", blank=True, null=True
    )  # Field name made lowercase.
    unitprice = models.TextField(
        db_column="UnitPrice"
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = "tracks"
