from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
# Create your views here.

def list_album(request):
    albums = Album.objects.all()
    return render(request, "albums/templates/albums/list_albums.html",
                  {"albums": albums})

