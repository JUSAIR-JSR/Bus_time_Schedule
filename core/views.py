from django.shortcuts import render
from Bus_root.models import MovieInfo

def view_all_buses(request):
    buses = MovieInfo.objects.all()
    return render(request, 'show.html', {'buses': buses})
