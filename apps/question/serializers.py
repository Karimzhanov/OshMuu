from rest_framework import serializers
from apps.question.models import Subject, Question

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        ref_name = 'QuestionSerializerFromQuestionApp'
