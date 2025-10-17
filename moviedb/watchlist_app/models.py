from django.db import models

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"<StreamPlatform {self.name}>"


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return f"<Movie {self.name}>"
    

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<WatchList {self.title}>"
    
