from django.urls import path

from apps.students.api.couse_student_api import CourseStudentAdminViewSet

# list_all_teacher = TeacherApiViewSet.as_view({'get': 'list_all_teachers'})
urlpatterns = [
    path('listar/cursos-student/', CourseStudentAdminViewSet.as_view({'get': 'list_course_student'})),
    ]