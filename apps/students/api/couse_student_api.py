from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse

from rest_framework.authtoken.models import Token

from apps.auth.models import UserProfile
from apps.students.models import CoursesStudents
from apps.students.serializers.course_student_serializer import ListCourseStudentSerializer
from apps.users.authentication_mixins import Authentication



class CourseStudentAdminViewSet(Authentication, viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def list_course_student(self, request):
        token_auth = request.META.get('HTTP_AUTHORIZATION').split()[1]
        token = Token.objects.filter(key=token_auth).first()

        user = UserProfile.objects.filter(id=token.user_id).first()
        cs = CoursesStudents.objects.filter(student_id=user.id).all()
        serializado = ListCourseStudentSerializer(cs, many=True).data

        return JsonResponse({'success': 'true', 'menu': serializado}, status=status.HTTP_200_OK)