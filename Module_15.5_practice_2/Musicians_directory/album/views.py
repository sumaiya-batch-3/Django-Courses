from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.

def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})


def edit_album(request, id):
    album_entry = Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album_entry)
    if request.method == "POST":
        album_form = AlbumForm(request.POST, instance=album_entry)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request, 'add_album.html', {'form': album_form})


def delete_album(request, id):
    album_entry = Album.objects.get(pk=id)
    album_entry.delete()
    return redirect('home')