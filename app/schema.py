from .types import ArtistType, ArtistInput, ArtistInputPartial, SongType
from typing import List
from strawberry_django_plus import gql


@gql.type
class Query:
    artist: ArtistType = gql.django.field()
    artist_filter: List[ArtistType] = gql.django.field()
    artists_pagination: gql.relay.Connection[ArtistType] = gql.relay.connection()
    artists_filter_relay: gql.relay.Connection[ArtistType] = gql.django.connection()
    songs: List[SongType] = gql.django.field()


@gql.type
class Mutation:
    create_artist: ArtistType = gql.django.create_mutation(ArtistInput)
    update_artist: ArtistType = gql.django.update_mutation(ArtistInputPartial)
    delete_artist: ArtistType = gql.django.delete_mutation(gql.NodeInput)
