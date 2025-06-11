from django.contrib import admin
from .models import Carousel, Image

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_public', 'created_at', 'updated_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'user__username')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('carousel', 'description', 'order', 'created_at')
    list_filter = ('carousel', 'created_at')
    search_fields = ('description', 'carousel__title')
