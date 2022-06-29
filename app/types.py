from strawberry_django_plus import gql
from typing import List
import models


@gql.django.type(models.Artist)
class ArtistType:
    name: gql.auto
    albums: 'List[AlbumType]'


@gql.django.type(models.Album)
class AlbumType:
    name: gql.auto
    release_date: gql.auto
    artist: ArtistType
    songs: 'List[SongType]'


@gql.django.type(models.Song)
class SongType:
    name: gql.auto
    duration: gql.auto
    album_type: 'AlbumType'


@gql.django.input(models.Artist)
class ArtistInput:
    name: gql.auto


@gql.django.input(models.Album)
class AlbumInput:
    name: gql.auto
    release_date: gql.auto


@gql.django.input(models.Song)
class SongInput:
    name: gql.auto
    duration: gql.auto


@gql.django.partial(models.Artist)
class ArtistInputPartial(gql.NodeInput):
    name: gql.auto


@gql.django.partial(models.Album)
class AlbumInputPartial(gql.NodeInput):
    name: gql.auto
    release_date: gql.auto


@gql.django.partial(models.Song)
class SongInputPartial(gql.NodeInput):
    name: gql.auto
    duration: gql.auto
