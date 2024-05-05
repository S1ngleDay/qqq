from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),  # Главная страница
    path('bugs/', views.bug_list, name='bug_list'),  # Маршрут для списка отчетов об ошибках (багах)
    path('features/', views.feature_list, name='feature_list'),  # Маршрут для списка запросов на улучшение
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('', views.IndexView.as_view(), name='index'),


    # path('projects/<int:project_id>/quality_control/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
]