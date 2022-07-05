import strawberry
import app.schema
from strawberry_django_plus import gql
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from gqlauth.user.queries import UserQueries
from gqlauth.user import relay
from strawberry.tools import merge_types


@gql.type
class Query(app.schema.Query, UserQueries):
    pass


@gql.type
class Mutation(app.schema.Mutation):
    token_auth = relay.ObtainJSONWebToken.Field  # login mutation
    verify_token = relay.VerifyToken.Field
    refresh_token = relay.RefreshToken.Field
    revoke_token = relay.RevokeToken.Field
    register = relay.Register.Field
    verify_account = relay.VerifyAccount.Field
    update_account = relay.UpdateAccount.Field
    resend_activation_email = relay.ResendActivationEmail.Field
    archive_account = relay.ArchiveAccount.Field
    delete_account = relay.DeleteAccount.Field
    password_change = relay.PasswordChange.Field
    send_password_reset_email = relay.SendPasswordResetEmail.Field
    password_reset = relay.PasswordReset.Field
    password_set = relay.PasswordSet.Field
    verify_secondary_email = relay.VerifySecondaryEmail.Field
    swap_emails = relay.SwapEmails.Field
    remove_secondary_email = relay.RemoveSecondaryEmail.Field
    send_secondary_email_activation = relay.SendSecondaryEmailActivation.Field


schema = strawberry.Schema(query=Query,
                           mutation=Mutation,
                           extensions=[DjangoOptimizerExtension])


