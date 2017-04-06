from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from forms import jobsPostForm, jobsBidForm
from .models import Job


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
        form = jobsPostForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.published_date = timezone.now()
            job.save()
            return redirect(job_detail, job.pk)

    else:
        form = jobsPostForm()
    return render(request, 'jobpostform.html', {'form': form})


def new_bid(request):
    if request.method == "POST":
        form = jobsBidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.owner = request.user
            bid.published_date = timezone.now()
            bid.save()
            return redirect(job_detail, bid.pk)

    else:
        form = jobsBidForm()
    return render(request, 'jobbidform.html', {'form': form})
