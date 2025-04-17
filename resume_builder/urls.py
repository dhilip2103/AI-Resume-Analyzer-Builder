from django.urls import path
from . import views

app_name = 'resume_builder'

urlpatterns = [
    path('select/', views.resume_selection, name='resume_selection'),
    path('workspace/<str:template_name>/', views.resume_workspace, name='resume_workspace'),
    path('preview/', views.resume_preview, name='resume_preview'),
]