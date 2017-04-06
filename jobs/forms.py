from django import forms

from .models import Job, Bid


class jobsPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'image', 'collection_point', 'destination_point', 'total_distance')


class jobsBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('bidder', 'bid_amount')
