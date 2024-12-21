from django import forms
from .models import MovieInfo

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieInfo
        fields = ['Bus_name', 'Bus_number', 'Bus_root', 'Bus_image', 'Bus_owner','Bus_time']
