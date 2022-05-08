from django.urls import path
from aplicatie3 import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobsView.as_view(), name='jobs_list'),
    path('add/', views.CreateJobsView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateJobsView.as_view(), name='update'),
    path('<int:pk>/delete/', views.delete_job, name='delete'),
    path('<int:pk>/activate/', views.activate_job, name='activate'),
]
