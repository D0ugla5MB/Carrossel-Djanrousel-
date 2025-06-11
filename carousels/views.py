from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .models import Carousel, Image
from django.contrib import messages

def index(request):
    # Show public carousels on the home page - accessible to all users
    public_carousels = Carousel.objects.filter(is_public=True).order_by('-created_at')[:6]
    return render(request, 'carousels/index.html', {'carousels': public_carousels})

def carousel_list(request):
    # For authenticated users, show their carousels along with public ones
    if request.user.is_authenticated:
        user_carousels = Carousel.objects.filter(user=request.user).order_by('-created_at')
        public_carousels = Carousel.objects.filter(is_public=True).exclude(user=request.user).order_by('-created_at')
        return render(request, 'carousels/carousel_list.html', {
            'user_carousels': user_carousels,
            'public_carousels': public_carousels
        })
    else:
        public_carousels = Carousel.objects.filter(is_public=True).order_by('-created_at')
        return render(request, 'carousels/carousel_list.html', {
            'public_carousels': public_carousels
        })

def carousel_detail(request, carousel_id):
    carousel = get_object_or_404(Carousel, id=carousel_id)
    
    # Check if user has permission to view this carousel
    if not carousel.is_public and (not request.user.is_authenticated or carousel.user != request.user):
        messages.error(request, "You don't have permission to view this carousel.")
        return redirect('carousels:index')
    
    images = carousel.images.all()
    return render(request, 'carousels/carousel_detail.html', {'carousel': carousel, 'images': images})

# Carousel CRUD operations
@login_required
def carousel_create(request):
    # Placeholder for carousel creation logic
    return HttpResponse("Carousel create view - to be implemented")

@login_required
def carousel_edit(request, carousel_id):
    # Placeholder for carousel edit logic
    return HttpResponse("Carousel edit view - to be implemented")

@login_required
def carousel_delete(request, carousel_id):
    # Placeholder for carousel deletion logic
    return HttpResponse("Carousel delete view - to be implemented")

# Image CRUD operations
@login_required
def image_add(request, carousel_id):
    # Placeholder for image addition logic
    return HttpResponse("Image add view - to be implemented")

@login_required
def image_edit(request, image_id):
    # Placeholder for image edit logic
    return HttpResponse("Image edit view - to be implemented")

@login_required
def image_delete(request, image_id):
    # Placeholder for image deletion logic
    return HttpResponse("Image delete view - to be implemented")
