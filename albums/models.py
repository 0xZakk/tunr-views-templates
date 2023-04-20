from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return self.title

