from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse

from apps.auth.models import UserProfile
from apps.courses.models import Modalidad, Ciclo, CoursesNames, Courses
from apps.courses.serializer.course_serializer import ListCoursesSerializer
from apps.users.authentication_mixins import Authentication
from apps.users.models import UserRol, NavBar


class StudentsInscripViewSet(Authentication, viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def list_all_Students(self, request):

        cantidad = int(request.query_params.get('cantidad'))
        pagina = int(request.query_params.get('pagina'))

        rol_student = NavBar.objects.filter(is_rol='is_student').first()
        if rol_student is None:
            return JsonResponse({'success': False, 'message': 'No se encontro el rol estudiante', 'data': None},
                                status=status.HTTP_400_BAD_REQUEST)

        estudiantes = UserRol.objects.filter(rol_id= rol_student.id).order_by('-id').all()
        # consulta = UserProfile.objects.filter().order_by('-id').all()
        # students_serializer = student_serializer.StudentSerializer(consulta, many=True).data
        # countt = UserProfile.objects.filter(is_student=True).all().count()
        #
        # paginacion = Paginator(students_serializer, cantidad)
        if len(paginacion.page(1)) == 0:
            return JsonResponse({'success': False, 'message': 'successful', 'data': None},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'success': True, 'cantidad': countt, 'data': (list(paginacion.page(pagina)))},
                                status=status.HTTP_200_OK)

        return JsonResponse({'success': 'true','message':'Se listo correctamente.', 'data':mod }, status=status.HTTP_200_OK)