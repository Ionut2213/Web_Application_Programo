from django.urls import path
from .import views

urlspatterns = [
    path('adauga_feedback/', views.add_feedback, name='add-feedback'),
    path('list_feedback/', views.list_feedback, name='list-feedback'),
    path('history/', views.history_feedback, name='history-feedback'),
]