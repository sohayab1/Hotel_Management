from django import forms
from .models import Review

#if  room is available book straight away,otherwise redirect to other section


class AvailabilityForm(forms.Form):
    
    check_in=forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M" ,])
    check_out=forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M" ,])
    
class ReviewForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1, max_value=5)