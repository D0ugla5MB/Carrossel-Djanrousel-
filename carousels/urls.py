from django.urls import path
from . import views

app_name = 'carousels'

urlpatterns = [
    # Home page showing public carousels
    path('', views.index, name='index'),
    
    # Carousel list and detail pages
    path('carousels/', views.carousel_list, name='carousel_list'),
    path('carousels/<int:carousel_id>/', views.carousel_detail, name='carousel_detail'),
    
    # Carousel management
    path('carousels/create/', views.carousel_create, name='carousel_create'),
    path('carousels/<int:carousel_id>/edit/', views.carousel_edit, name='carousel_edit'),
    path('carousels/<int:carousel_id>/delete/', views.carousel_delete, name='carousel_delete'),
    
    # Image management
    path('carousels/<int:carousel_id>/images/add/', views.image_add, name='image_add'),
    path('images/<int:image_id>/edit/', views.image_edit, name='image_edit'),
    path('images/<int:image_id>/delete/', views.image_delete, name='image_delete'),
]
