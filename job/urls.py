from django.urls import path;
from . import views;

urlpatterns = [
     path("", views.jobs_page),
     path("<int:id>", views.job_info),
]