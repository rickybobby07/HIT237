from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project-list'),
    path('project/<int:topic_id>', views.project_detail, name="project")
]
