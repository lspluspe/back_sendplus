from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse

from rest_framework.authtoken.models import Token
from apps.users.authentication_mixins import Authentication

from apps.auth.models import UserProfile
from apps.users.models import UserRol
from apps.users.serializer import nav_bar_serializer


class NavigationBarViewSet(Authentication, viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def list_nav_roles(self, request):
        token_auth = request.META.get('HTTP_AUTHORIZATION').split()[1]
        token = Token.objects.filter(key=token_auth).first()
        user = UserProfile.objects.filter(id=token.user_id).first()
        navs = UserRol.objects.filter(user_id=user.id).all()
        rol_serializer = nav_bar_serializer.UserRolSerializer(navs,many=True).data

        return JsonResponse({'success': 'true', 'menu': rol_serializer}, status=status.HTTP_200_OK)