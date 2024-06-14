from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet, TestResultViewSet
from apps.question.views import QuestionAPIViews

router = DefaultRouter()
router.register(r'tests', TestViewSet, basename='test')
router.register(r'results', TestResultViewSet, basename='result')

urlpatterns = [
    path('tests/<int:test_id>/questions/', QuestionAPIViews.as_view({'post': 'create', 'get': 'list'}), name='test-questions'),
    path('tests/<int:test_id>/questions/<int:pk>/', QuestionAPIViews.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='test-question-detail'),
]

urlpatterns += router.urls
