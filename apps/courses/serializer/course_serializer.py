from rest_framework import serializers

from apps.courses.models import Modalidad, Ciclo, CoursesNames, CourseDetail, Courses
from apps.users.models import NavBar, UserRol


class ListModalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidad
        fields = '__all__'


class ListCiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo
        fields = '__all__'

class ListCoursesNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesNames
        fields = '__all__'

class ListCourseDetailSerializer(serializers.ModelSerializer):
    ciclo=ListCiclesSerializer(many=False)
    tipo_modalidad= ListModalidadSerializer(many=False)
    courses_name= ListCoursesNamesSerializer(many=False)
    class Meta:
        model = CourseDetail
        fields = '__all__'


class ListCoursesSerializer(serializers.ModelSerializer):
    course_detail = ListCourseDetailSerializer(many=False)
    class Meta:
        model = Courses
        fields = '__all__'