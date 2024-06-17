from django.urls import path, include
from .views import GenreView, LicenseViewSets, AlbumViewSets


urlpatterns = [
    path('genre/', GenreView.as_view()),

    path('license/', LicenseViewSets.as_view({'get': 'list', 'post': 'create'})),
    path('license/<int:pk>/', LicenseViewSets.as_view({'put': 'update', 'delete': 'destroy'})),

    path('album/', AlbumViewSets.as_view({'get': 'list', 'post': 'create'})),
    path('album/<int:pk>/', AlbumViewSets.as_view({'put': 'update', 'delete': 'destroy'})),
]