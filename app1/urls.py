from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    
    path('categoria/', views.categoria, name='categoria'),
    path('categoria/edit/<int:pk>/', views.categoria, name='categoria-edit'),
    path('categoria/delete/<int:pk>/', views.categoria, name='categoria-delete'),

    path('autor/', views.autor, name='autor'),
    path('autor/edit/<int:pk>/', views.autor, name='autor-edit'),
    path('autor/delete/<int:pk>/', views.autor, name='autor-delete'),

    path('libro/', views.libro, name='libro'),
    path('libro/edit/<int:pk>/', views.libro, name='libro-edit'),
    path('libro/delete/<int:pk>/', views.libro, name='libro-delete'),

    path('prestamo/', views.prestamo, name='prestamo'),
    path('prestamo/edit/<int:pk>/', views.prestamo, name='prestamo-edit'),
    path('prestamo/delete/<int:pk>/', views.prestamo, name='prestamo-delete')
]