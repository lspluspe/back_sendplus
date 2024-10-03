from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse

from apps.academico.models import ClasesCourses
from apps.courses.models import Modalidad, Ciclo, CoursesNames, Courses, Modules
from apps.courses.serializer.course_serializer import ListCoursesSerializer
from apps.users.authentication_mixins import Authentication



class InformationCouseViewSet(Authentication, viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def list_modalidad(self, request):
        mod = list(Modalidad.objects.all().values())
        return JsonResponse({'success': True,'message':'Se listo correctamente.', 'data':mod }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_ciclos(self, request):
        cicles = list(Ciclo.objects.all().values())
        return JsonResponse({'success': True,'message':'Se listo correctamente.', 'data':cicles }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_courses_names(self, request):
        names = list(CoursesNames.objects.all().values())
        return JsonResponse({'success': True,'message':'Se listo correctamente.', 'data':names  }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_courses(self, request):
        names = Courses.objects.all()
        course_serializer = ListCoursesSerializer(names, many=True).data
        return JsonResponse({'success': True, 'message': 'Se listo correctamente.', 'data': course_serializer},
                            status=status.HTTP_200_OK)

    def list_courses_detail(self, request,pk):
        course = Courses.objects.filter(id=pk).first()
        if course is None:
            return JsonResponse({'success': False, 'message': 'Curso no encontrado', 'data': None},
                                status=status.HTTP_200_OK)
        modulos = list(Modules.objects.filter(course_id=course.id).order_by('module_number').all().values('id','module_number','module_name'))
        for i in modulos:
            clases = list(ClasesCourses.objects.filter(module_id=i['id']).order_by('num_class').all().values('num_class','detail','is_virtual'))
            i['clases']=clases

        course_serializer = ListCoursesSerializer(course, many=False).data
        course_serializer['modulos'] = modulos
        return JsonResponse({'success': True, 'message': 'Se listo correctamente.', 'data':course_serializer },
                            status=status.HTTP_200_OK)
