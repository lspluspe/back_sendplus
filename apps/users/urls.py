
from django.urls import path

from apps.users.views import Login

# list_all_teacher = TeacherApiViewSet.as_view({'get': 'list_all_teachers'})
urlpatterns = [
    path('login/', Login.as_view(), name='login/'),
    # path('listar-todos-docentes/', list_all_teacher, name="listar-todos-docentes/"),
    ]
