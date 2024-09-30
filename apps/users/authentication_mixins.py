from rest_framework import status
from rest_framework.authentication import get_authorization_header
from apps.users.authentication import ExpiringTokenAuthentication
from django.http import JsonResponse


class Authentication(object):
    user = None
    user_token_expired = False

    def get_user(self, request):
        """
            token = get_authorization_header(request).split()
            token = token[1].decode
        :param request:
        :return:
        """
        # token =request.META.get('HTTP_AUTHORIZATION').split()
        token = get_authorization_header(request).split()
        if token:
            try:
                # token = token[1]
                token = token[1].decode()
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            user, token, message, self.user_token_expired = token_expire.authenticate_credentials(token)
            if user != None and token != None and self.user_token_expired != True:
                self.user = user
                return user
            if self.user_token_expired:
                message = 'Token expirado'
            return message
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        # Se enecontro un token en request
        if user is not None:
            if type(user) == str:
                return JsonResponse({'error': user}, status=status.HTTP_401_UNAUTHORIZED)
            return super().dispatch(request, *args, **kwargs)
        return JsonResponse({'error': 'No se han enviado las credenciales.', 'user': user},
                            status=status.HTTP_400_BAD_REQUEST)
