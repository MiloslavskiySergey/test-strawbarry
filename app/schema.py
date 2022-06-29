from .types import ArtistType, ArtistInput, ArtistInputPartial, SongType
from .models import Artist
from typing import List
from strawberry_django_plus import gql


@gql.type
class Query:
    artist: Artist = gql.django.field()
    songs: List[SongType] = gql.django.field()


@gql.type
class Mutation:
    create_artist: ArtistType = gql.django.create_mutation(ArtistInput)
    update_artist: ArtistType = gql.django.update_mutation(ArtistInputPartial)
    delete_artist: ArtistType = gql.django.delete_mutation(gql.NodeInput)
