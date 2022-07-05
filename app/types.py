from strawberry_django_plus import gql
from typing import List, Optional
from .models import Artist, Album, Song
from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from strawberry.types.info import Info
from strawberry_django_plus.permissions import (
    HasObjPerm,
    HasPerm,
    IsAuthenticated,
    IsStaff,
    IsSuperuser,
)

from django.contrib.auth import get_user_model


@gql.django.type(get_user_model())
class UserType:
    username: gql.auto
    email: gql.auto
    is_active: gql.auto
    is_superuser: gql.auto
    is_staff: gql.auto


@gql.django.input(get_user_model())
class UserInput:
    username: gql.auto
    email: gql.auto
    password: gql.auto
    is_active: gql.auto
    is_superuser: gql.auto
    is_staff: gql.auto


@gql.django.filter(Artist, lookups=True)
class ArtistFilter:
    name: gql.auto
    albums: gql.auto
    totalCount: Optional[str]
    # search: Optional[str]
    #
    # def filter_search(self, queryset: QuerySet[Artist]):
    #     return queryset.filter(name__contains=self.search)


@gql.django.order(Artist)
class ArtistOrder:
    name: gql.auto
    albums: 'AlbumOrder | None'


@gql.django.type(Artist, filters=ArtistFilter, order=ArtistOrder)
class ArtistType(gql.relay.Node):
    name: gql.auto
    albums: 'list[AlbumType] | None'


@gql.django.input(Artist)
class ArtistInput:
    name: gql.auto


@gql.django.partial(Artist)
class ArtistInputPartial(gql.NodeInput):
    name: gql.auto


@gql.django.order(Album)
class AlbumOrder:
    name: gql.auto
    release_date: gql.auto


@gql.django.type(Album)
class AlbumType:
    name: gql.auto
    release_date: gql.auto
    artist: ArtistType | None
    songs: 'list[SongType] | None' = gql.django.field(directives=[IsAuthenticated()])


@gql.django.input(Album)
class AlbumInput:
    name: gql.auto
    release_date: gql.auto


@gql.django.partial(Album)
class AlbumInputPartial(gql.NodeInput):
    name: gql.auto
    release_date: gql.auto


@gql.django.type(Song)
class SongType:
    name: gql.auto
    duration: gql.auto
    album_type: 'AlbumType | None'


@gql.django.input(Song)
class SongInput:
    name: gql.auto
    duration: gql.auto


@gql.django.partial(Song)
class SongInputPartial(gql.NodeInput):
    name: gql.auto
    duration: gql.auto
