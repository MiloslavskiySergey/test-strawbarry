from django.db import models


class Artist(models.Model):
    name = models.CharField()


class Album(models.Model):
    name = models.CharField()
    release_date = models.DateTimeField()
    artist = models.ForeignKey("Artist", related_name="albuns", on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField()
    duration = models.DecimalField()
    album = models.ForeignKey("Album", related_name="songs", on_delete=models.CASCADE)
