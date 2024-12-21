from django.shortcuts import render
from Bus_root.models import MovieInfo
from datetime import datetime

def view_all_buses(request):
    current_time = datetime.now().time()
    # Get future and past buses
    future_buses = MovieInfo.objects.filter(Bus_time__gte=current_time).order_by('Bus_time')
    past_buses = MovieInfo.objects.filter(Bus_time__lt=current_time).order_by('Bus_time')
    # Combine future and past buses, so future buses come first
    buses = list(future_buses) + list(past_buses)
    return render(request, 'show.html', {'buses': buses, 'current_time': current_time})
