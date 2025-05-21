from django.urls import path

from . import views
from .views import delete_pacient


urlpatterns = [
    path('create_pacient/', views.PacientCreateView.as_view(), name='create-pacient'),
    path('list_pacients/', views.PacientListView.as_view(), name='list-pacients'),
    path('update_pacient/<int:pk>/', views.PacientUpdateView.as_view(), name='update-pacient'),
    path('delete_pacient/<int:pk>/', views.PacientDeleteView.as_view(), name='delete-pacient'),
]