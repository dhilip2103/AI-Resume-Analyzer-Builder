from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.resume_selection, name='resume_selection'),
    path('edit/', views.resume_editor, name='resume_editor'), 
    path('preview/', views.resume_preview, name='preview'),
    path('download/<str:format>/', views.download_resume, name='export_resume'),
]