from rest_framework import mixins, viewsets, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.tests.models import Test, TestResult
from apps.tests.serializers import TestSerializer, TestCreateUpdateSerializer, TestResultSerializer
from apps.question.models import Question, Subject
from apps.users.models import Employee
from apps.users.permissions import IsTeacher, IsStudent
import random

class TestViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsTeacher()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        subject_id = request.data.get('subject')
        subject = get_object_or_404(Subject, id=subject_id)
        
        question_ids = request.data.get('questions', [])
        questions = list(Question.objects.filter(subject=subject, id__in=question_ids))
        
        if len(questions) < 3:
            return Response(
                {"detail": "Недостаточно вопросов для создания теста."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        selected_questions = random.sample(questions, 3)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        test = serializer.save()
        
        test.questions.set(selected_questions)
        test.save()

        serializer = self.get_serializer(test)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        if not request.user.user_employee.employee_position == Employee.EmployeePositionChoice.TEACHER or instance.created_by != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.user_employee.employee_position == Employee.EmployeePositionChoice.TEACHER or instance.created_by != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestResultViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.IsAuthenticated(), IsStudent()]
        return [permissions.IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        user = request.user
       
