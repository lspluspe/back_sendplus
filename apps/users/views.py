from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken

import time

from apps.users.models import UserProfile
from apps.users.serializer import user_serializers


# Create your views here.



class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = user_serializers.UserTokenSerializer(user)
                if created:
                    user = UserProfile.objects.filter(id=token.user_id).first()
                    user.last_login_timetamps_unix = time.time()
                    user.save()
                    return JsonResponse({
                        'success': True,
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return JsonResponse({
                        'success': True,
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'errors': 'no_active',
                                     'message': 'Este usuario no puede iniciar sesión'
                                     }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({'error': 'Nomre de usuario o contraseña no incorrectos'},
                                status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):

    def get(self, request, *args, **kwargs):
        try:
            token = Token.objects.filter(key=request.GET.get('token')).first()
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return JsonResponse({'success': True, 'token_message': token_message, 'session_message': session_message},
                                    status=status.HTTP_200_OK)
            return JsonResponse({'success': False, 'message': 'No se ha encontrado un usuario con estas credenciales'},
                                    status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({'success': False, 'message': 'No se ha encontrado un token en la peticion'},
                                status=status.HTTP_409_CONFLICT)
