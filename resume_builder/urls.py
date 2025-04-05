from django.urls import path
from . import views

urlpatterns = [
    path('select/', views.resume_selection, name='resume_selection'),
    path('workspace/<str:template_name>/', views.resume_workspace, name='resume_workspace'),
    #path('edit/<int:template_id>/', views.edit_resume, name='edit_resume'),
]