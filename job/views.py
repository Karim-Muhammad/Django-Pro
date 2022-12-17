from django.shortcuts import render
from .models import Job;
# Create your views here.

def jobs_page(request):
     jobs = Job.objects.all();
     return render(request, "jobs.html", {"jobs": jobs})

def job_info(request, id):
     job = Job.objects.all()[id-1]
     return render(request, "job.html", {"job": job})