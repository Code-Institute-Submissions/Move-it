# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone



# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     views = models.IntegerField(default=0)
#     tag = models.CharField(max_length=30, blank=True, null=True)
#     image = models.ImageField(upload_to="images", blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __unicode__(self):
#         return self.title


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to="images", blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    collection_point = models.CharField(max_length=200, blank=True, null=True)
    destination_point = models.CharField(max_length=200, blank=True, null=True)
    total_distance = models.IntegerField(default=1)
    def __unicode__(self):
        return self.title


class Bid(models.Model):
    job = models.ForeignKey(Job)
    bidder = models.ForeignKey('auth.User')
    published_date = models.DateTimeField(blank=True, null=True)
    bid_amount = models.IntegerField(default=1)

    def __unicode__(self):
        return "{0} bid  {1} for job {2} ".format(self.bidder.username, self.bid_amount, self.title)