from django.urls import path

from apps.courses.api.information_couse_api import InformationCouseViewSet


urlpatterns = [
    path('listar/modalidad/', InformationCouseViewSet.as_view({'get': 'list_modalidad'})),
    path('listar/ciclos/', InformationCouseViewSet.as_view({'get': 'list_ciclos'})),
    path('listar/nombres-cursos/', InformationCouseViewSet.as_view({'get': 'list_courses_names'})),
    path('listar/cursos-detallado/<int:pk>', InformationCouseViewSet.as_view({'get': 'list_courses_detail'})),
    ]