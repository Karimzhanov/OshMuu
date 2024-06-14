from rest_framework import serializers # type: ignore
from .models import TestResult

class TestResultSerializer(serializers.ModelSerializer):
    test_name = serializers.ReadOnlyField(source='test.name')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TestResult
        fields = ['test_id', 'test_name', 'user_id', 'username', 'score', 'completed_at']
