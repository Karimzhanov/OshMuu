from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .models import TestResult
from .serializers import TestResultSerializer
import csv

class ResultsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_teacher:
            results = TestResult.objects.all()
            serializer = TestResultSerializer(results, many=True)
            return Response(serializer.data)
        return Response(status=403)

class TestResultsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, test_id):
        results = TestResult.objects.filter(test_id=test_id)
        if request.user.is_teacher or request.user.id in results.values_list('user_id', flat=True):
            serializer = TestResultSerializer(results, many=True)
            return Response(serializer.data)
        return Response(status=403)

class ExportResultsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, test_id):
        format = request.query_params.get('format', 'csv')
        results = TestResult.objects.filter(test_id=test_id)
        if not request.user.is_teacher:
            return Response(status=403)
        
        if format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="test_{test_id}_results.csv"'

            writer = csv.writer(response)
            writer.writerow(['test_id', 'test_name', 'user_id', 'username', 'score', 'completed_at'])
            for result in results:
                writer.writerow([result.test_id, result.test.name, result.user_id, result.user.username, result.score, result.completed_at])
            
            return response
        
        # Для PDF можно использовать библиотеку ReportLab или аналогичные
        # ...

        return Response(status=400)
