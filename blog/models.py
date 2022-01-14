from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    
    def __str__(self):
        return self.title

    
