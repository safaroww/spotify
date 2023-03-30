from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customer/images/', null=True, blank=True)
    liked_songs = models.ManyToManyField('song.Song', related_name='liked_customers') 
    liked_playlists = models.ManyToManyField('song.Playlist', related_name='liked_customers')
    followed_artists = models.ManyToManyField('Artist', related_name='followers')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    

class Artist(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artist/images/', null=True, blank=True)
    cover = models.ImageField(upload_to='artist/covers/') 
    color = ColorField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    verified = models.BooleanField(default=False)


