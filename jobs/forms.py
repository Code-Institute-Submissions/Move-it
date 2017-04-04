from django import forms
from .models import Job

class jobsPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'image', 'collection_point', 'destination_point', 'total_distance')




