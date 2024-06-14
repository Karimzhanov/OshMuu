from rest_framework import serializers
from apps.tests.models import Test, TestResult
from apps.question.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        ref_name = 'QuestionSerializerFromTestApp'

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = '__all__'

class TestCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        exclude = ('created_by',)

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'