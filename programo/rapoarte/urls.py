from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_report, name='generate-report'),
    # path('list/', views.report_list, name= 'list-reports'),
    # path('rapoarte/<int:pk>/', views.report_details, name= 'report-detail'),
]