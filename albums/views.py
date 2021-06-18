from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
# Create your views here.

def list_album(request):
    albums = Album.objects.all()
    return render(request, "albums/templates/albums/list_albums.html",
                {"albums": albums})

def new_album(request):
    
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/templates/albums/add_album.html", {"form": form})

