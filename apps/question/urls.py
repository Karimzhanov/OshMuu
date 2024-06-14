from rest_framework.routers import DefaultRouter
from apps.question.views import SubjectAPIViews, QuestionAPIViews

router = DefaultRouter()
router.register('subject', SubjectAPIViews, basename='api_subject')
router.register('question', QuestionAPIViews, basename='api_question')

urlpatterns = router.urls
