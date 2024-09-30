from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse

from rest_framework.authtoken.models import Token

from apps.courses.models import Modalidad, Ciclo, CoursesNames
from apps.users.authentication_mixins import Authentication



class InformationCouseViewSet(Authentication, viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def list_modalidad(self, request):
        mod = list(Modalidad.objects.all().values())
        return JsonResponse({'success': 'true','message':'Se listo correctamente.', 'data':mod }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_ciclos(self, request):
        cicles = list(Ciclo.objects.all().values())
        return JsonResponse({'success': 'true','message':'Se listo correctamente.', 'data':cicles }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_courses_names(self, request):
        names = list(CoursesNames.objects.all().values())
        return JsonResponse({'success': 'true','message':'Se listo correctamente.', 'data':names  }, status=status.HTTP_200_OK)