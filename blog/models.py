from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images', blank=True)
    post = models.TextField()

    def __str__(self):
        return self.title