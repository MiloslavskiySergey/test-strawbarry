from .types import ArtistType,\
    ArtistInput,\
    ArtistInputPartial,\
    SongType,\
    UserType,\
    UserInput,\
    ArtistFilter,\
    ArtistOrder
from typing import List, Optional
from strawberry_django_plus import gql
from strawberry_django.auth import login, logout, current_user, register


@gql.type
class Query:
    artist: ArtistType = gql.django.field()
    artist_filter: List[ArtistType] = gql.django.field(order=ArtistOrder,
                                                       filters=ArtistFilter,
                                                       pagination=True)
    artists_pagination: gql.relay.Connection[ArtistType] = gql.relay.connection()
    artists_filter_relay: gql.relay.Connection[ArtistType] = gql.django.connection()
    songs: List[SongType] = gql.django.field()

    user: UserType = current_user()


@gql.type
class Mutation:
    create_artist: ArtistType = gql.django.create_mutation(ArtistInput)
    update_artist: ArtistType = gql.django.update_mutation(ArtistInputPartial)
    delete_artist: ArtistType = gql.django.delete_mutation(gql.NodeInput)

    login: UserType = login()
    logout: UserType = logout()
    register: UserType = register(UserInput)
