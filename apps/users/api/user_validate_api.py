from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from apps.auth.models import UserProfile

import decimal
import datetime

import logging
from rest_framework import status


class UserValidateViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def validar_usuario_login(self, request):
        rd=request.query_params.get
        if UserProfile.objects.filter(usuario=rd('usuario')).exists():
            return JsonResponse({'success': True, 'Message':'Usuario Encontrado!' ,},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse({'success': False, 'Message': 'Usuario no encontrado, vuelva a Ingresar!', },
                                status=status.HTTP_400_BAD_REQUEST)