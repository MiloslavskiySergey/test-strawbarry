from strawberry_django_plus import gql
from typing import List
from .models import Artist, Album, Song


@gql.django.type(Artist)
class ArtistType:
    name: gql.auto
    albums: 'List[AlbumType]'


@gql.django.type(Album)
class AlbumType:
    name: gql.auto
    release_date: gql.auto
    artist: ArtistType
    songs: 'List[SongType]'


@gql.django.type(Song)
class SongType:
    name: gql.auto
    duration: gql.auto
    album_type: 'AlbumType'


@gql.django.input(Artist)
class ArtistInput:
    name: gql.auto


@gql.django.input(Album)
class AlbumInput:
    name: gql.auto
    release_date: gql.auto


@gql.django.input(Song)
class SongInput:
    name: gql.auto
    duration: gql.auto


@gql.django.partial(Artist)
class ArtistInputPartial(gql.NodeInput):
    name: gql.auto


@gql.django.partial(Album)
class AlbumInputPartial(gql.NodeInput):
    name: gql.auto
    release_date: gql.auto


@gql.django.partial(Song)
class SongInputPartial(gql.NodeInput):
    name: gql.auto
    duration: gql.auto
