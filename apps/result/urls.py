from django.urls import path
from .views import ResultsListView, TestResultsView, ExportResultsView

urlpatterns = [
    path('results/', ResultsListView.as_view(), name='results_list'),
    path('results/<int:test_id>/', TestResultsView.as_view(), name='test_results'),
    path('results/<int:test_id>/export/', ExportResultsView.as_view(), name='export_results'),
]
