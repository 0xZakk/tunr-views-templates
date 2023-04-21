from django.shortcuts import render, redirect
from .models import Artist, Album
from .forms import ArtistForm

# Create your views here.
# List view for Artists
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'albums/artist_list.html', {'artists': artists})

def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'albums/artist_detail.html', {'artist': artist})

def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST) # request.body from express
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()

    return render(request, 'albums/artist_form.html', {'form': form})

def artist_edit(request, pk):
    artist = Artist.objects.get(id=pk)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'albums/artist_form.html', {'form': form})

def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')

# List view for Albums
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = Album.objects.get(id=pk)
    return render(request, 'albums/album_detail.html', {'album': album})
