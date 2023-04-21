from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('artists/new', views.artist_create, name='artist_create'),
    path('artist/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    path('artist/<int:pk>/delete', views.artist_delete, name='artist_delete'),
    path('albums', views.album_list, name='album_list'),
    path('albums/<int:pk>', views.album_detail, name='album_detail')
]
