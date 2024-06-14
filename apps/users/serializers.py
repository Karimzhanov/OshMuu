from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password

from apps.users.models import User, Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'last_login', 'username', 
                  'first_name', 'last_name', 
                  'email')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username',  'first_name',
                  'last_name', 'email')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id',  'username', 
                  'first_name', 'last_name',
                  'email',  )
    
class UserRegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=250, write_only=True)
    confirm_password = serializers.CharField(max_length=255, write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        elif len(attrs['password']) < 8 and len(attrs['confirm_password']) < 8:
            raise serializers.ValidationError({'password_len': 'Длина пароля меньше 8'})
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    


class UserRegistrationResponseSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email','refresh', 'access')

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'