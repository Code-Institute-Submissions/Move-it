from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.job_list, name='job_list'),
    url(r'^jobs/new/$', views.new_job, name='new_job'),
    url(r'^jobs/(?P<id>\d+)/$', views.job_detail, name='job_detail'),
    url(r'^jobs/(?P<id>\d+)/bid/$', views.new_bid, name='new_bid'),
]
