from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from forms import jobsPostForm
from .models import Job, Bid



# Create your views here.

def job_list(request):
    jobs = Job.objects.filter(published_date__lte=timezone.now()
                              ).order_by('-published_date')
    return render(request, "jobposts.html", {'jobs': jobs})


def job_detail(request, id):
    job = get_object_or_404(Job, pk=id)
    return render(request, "viewjob.html", {'job': job})


def new_job(request):
    if request.method == "POST":
        form = jobsPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.author = request.user
            job.published_date = timezone.now()
            return redirect(job_list, job.pk)

    else:
        form = jobsPostForm()
    return render(request, 'jobpostform.html', {'form': form})


