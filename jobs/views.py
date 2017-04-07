from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

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


# def new_bid(request):
#     if request.method == "POST":
#         form = jobsBidForm(request.POST, request.FILES)
#         if form.is_valid():
#             bid = form.save(commit=False)
#             bid.owner = request.user
#             bid.published_date = timezone.now()
#             bid.save()
#             return redirect(job_detail, bid.pk)
#
#     else:
#         form = jobsBidForm()
#     return render(request, 'jobbidform.html', {'form': form})

@login_required(login_url="/accounts/login")
def new_bid(request, id):
    job = get_object_or_404(Job, pk=id)
    bid_amount = int(request.POST.get('amount'))

    bid = Bid(
        bidder=request.user,
        job=job,
        bid_amount=bid_amount
    )
    messages.success(request, 'You have successfully made a bid ')
    bid.save()

    return redirect(job_detail, job.id)