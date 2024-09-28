from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

from apps.users.models import UserProfile, UrlPassword


class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('usuario', 'name', 'phone', 'email', 'detail_user')

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email', 'name', 'usuario', 'phone', 'is_superuser', 'is_staff',)


class InfoUserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'detail_user')


class SaveConfigInitial(serializers.Serializer):
    profession = serializers.CharField(max_length=100)
    consejo_reginal_colegiatura = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    num_colegiatura = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    centro_laboral = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)


class UpdateConfigInitial(serializers.Serializer):

    num_colegiatura = serializers.CharField(max_length=100, required=False)
    consejo_nacional= serializers.CharField(max_length=100, required=False)


class ChangePasswordSerializer(serializers.Serializer):
    old_pasword = serializers.CharField(max_length=100, required=True)
    new_password = serializers.CharField(max_length=100, required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class SendEmailToResetSerializer(serializers.Serializer):
    num_documento = serializers.CharField(max_length=18)

    def validate(self, attrs):
        """ Validar si existe el numero de documento"""

        num_doc = attrs.get('num_documento')

        if UserProfile.objects.filter(usuario=num_doc).exists():
            return True
        else:
            raise serializers.ValidationError("No Existe el número de docuento")


class ResetPassword(serializers.Serializer):
    new_password = serializers.CharField(max_length=20)
    url_code = serializers.CharField(max_length=64)

    def validate(self, attrs):
        """ Validar si existe el numero de documento"""

        url_code = attrs.get('url_code')

        if UrlPassword.objects.filter(url_code=url_code).exists():
            return True
        else:
            raise serializers.ValidationError("No existe el codigo de url en nuestra base de datos")


class ValidateCodeSerializer(serializers.Serializer):
    url_code = serializers.CharField(max_length=64, required=True)

    def validate(self, attrs):
        url_code = attrs.get('url_code')
        if UrlPassword.objects.filter(url_code=url_code).exists():
            return True
        else:
            raise serializers.ValidationError("No existe el codigo de url en nuestra base de datos")
