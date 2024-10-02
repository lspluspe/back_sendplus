from rest_framework import serializers

from apps.courses.models import Modalidad, Ciclo, CoursesNames, CourseDetail, Courses
from apps.courses.serializer.course_serializer import ListCoursesSerializer
from apps.students.models import CoursesStudents
from apps.users.models import NavBar, UserRol


class ListCourseStudentSerializer(serializers.ModelSerializer):
    course = ListCoursesSerializer(many=False)
    class Meta:
        model = CoursesStudents
        fields = '__all__'