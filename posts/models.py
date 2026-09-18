from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    class PostType(models.TextChoices):
        VIDEO = "Vid", "Video"
        SOUND = "Music", "Sound"
        IMAGE = "Gif", "Gifs"
        FREE = "Free", "Freestyle"

    # ne lasa sa alegem ce tip de postare o sa fie si cu ajutorul ei o vom putea filtra
    post_type = models.CharField(choices=PostType.choices,max_length=5)

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    unique_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title