from rest_framework import serializers

from apps.users.models import NavBar, UserRol


class LisNavBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavBar
        fields = '__all__'


class UserRolSerializer(serializers.ModelSerializer):
    rol = LisNavBarSerializer(many=False)
    class Meta:
        model = UserRol
        fields = '__all__'