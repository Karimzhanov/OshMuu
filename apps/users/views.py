from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from apps.users.models import User, Employee
from apps.users import serializers

# Create your views here.
from apps.users.models import User
from apps.users import serializers

class UserViewsSet(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated, )
    
    def get_serializer_class(self):
        if self.action == 'create': 
            return serializers.UserRegisterSerializers
        if self.action == 'retrieve':
            return serializers.UserDetailSerializer
        if self.action in ('partial_update', 'update'):
            return serializers.UserUpdateSerializer
        return serializers.UserSerializer
    
    def get_permissions(self):
        if self.action == "create":
            return (AllowAny(), )
        elif self.action in ("partial_update", "update"):
            return (IsAuthenticated(), )
        return super().get_permissions()  # Ensure this always returns permissions
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = serializer.get_tokens_for_user(user)
        user_data = serializers.UserRegistrationResponseSerializer(user, context={'request': request}).data
        user_data.update(tokens)
        headers = self.get_success_headers(serializer.data)
        return Response(user_data, status=status.HTTP_201_CREATED, headers=headers)
    
class EmployeeAPIViews(GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                  ):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializers
    # permission_classes = (IsAuthenticated, )