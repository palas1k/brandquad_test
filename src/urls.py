from django.urls import path
from rest_framework.routers import DefaultRouter

from src import views

urlpatterns = [
    path('logs/', views.LogsViewSet.as_view({'get': 'list',
                                             'post': 'create'})),
]
