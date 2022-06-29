from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=20)


class Album(models.Model):
    name = models.CharField(max_length=20)
    release_date = models.DateTimeField()
    artist = models.ForeignKey("Artist", related_name="albuns", on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField(max_length=20)
    duration = models.DecimalField(decimal_places=10, max_digits=10)
    album = models.ForeignKey("Album", related_name="songs", on_delete=models.CASCADE)
