from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expired_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            # user = token.user
            self.expired = True
            token.delete()
            # token = self.get_model().objects.create(user=user)
        return is_expire

    def authenticate_credentials(self, key):
        message,token,user = None, None, None

        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user

        except self.get_model().DoesNotExist:
            message = 'Token inválido.'

        if token is not None:

            is_expired = self.token_expired_handler(token)
            if is_expired:
                message = 'Su token ha expirado.'
                return (None, None, message, self.expired)

            if not token.user.is_active:
                message = 'Usuario no activo o eliminado.'
                return (None, None, message, self.expired)

        return (user,token,message,self.expired)

