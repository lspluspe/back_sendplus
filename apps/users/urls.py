
from django.urls import path

from apps.users.api.navigation_bar_api import NavigationBarViewSet
from apps.users.api.user_validate_api import UserValidateViewSet
from apps.users.views import Login

# list_all_teacher = TeacherApiViewSet.as_view({'get': 'list_all_teachers'})
urlpatterns = [
    path('login/', Login.as_view(), name='login/'),
    path('listar/roles-menu/', NavigationBarViewSet.as_view({'get': 'list_nav_roles'})),
    path('validate-user/', UserValidateViewSet.as_view({'get': 'validar_usuario_login'})),
    ]
