from django.shortcuts import render, get_object_or_404, redirect
from .models import MovieInfo
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.created_by = request.user
            movie.save()
            return redirect('index.html')
    else:
        form = MovieForm()
    return render(request, 'create.html', {'form': form})

@login_required
def show(request):
    Buses = MovieInfo.objects.all()
    return render(request, 'index.html', {'Buses': Buses})

@login_required
def edit(request, pk):
    movie = get_object_or_404(MovieInfo, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form})

@login_required
def delete(request, pk):
    movie = get_object_or_404(MovieInfo, pk=pk, created_by=request.user)
    if request.method == "POST":
        movie.delete()
        return redirect('show')
    return render(request, 'delete.html', {'movie': movie})
