from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Movie
from django.contrib import messages
from .forms import MovieForm 

# Create your views here.
def home(request):
    movie=Movie.objects.all()
    context={
        'mlist':movie
    }
    return  render(request,"index.html",context)
def get_id(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        'movie': movie
    }
    return render(request, "detail.html", context)

def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('movieName')
        des = request.POST.get('description')
        yr = int(request.POST['year'])
        ig = request.FILES['image']
        movie = Movie(name=name, desc=des, year=yr, img=ig)  
        movie.save()  

        messages.info(request, 'Data uploaded successfully.')

        
        return redirect('home')  

    return render(request, "add.html")

def update(request, id):
    movie = Movie.objects.get(id=id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = MovieForm(instance=movie)

    return render(request, "edit.html", {'form': form, 'movie': movie})


def delete(request,id):
     if request.method == 'POST':
         movie = Movie.objects.get(id=id)
         movie.delete()
         messages.success(request, 'Movie deleted successfully.')
         return redirect('/')
     return render(request,'delete.html')










