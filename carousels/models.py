from django.db import models
from django.contrib.auth.models import User

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carousels')
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='carousel_images/')
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        
    def __str__(self):
        return f"Image {self.id} - {self.carousel.title}"
