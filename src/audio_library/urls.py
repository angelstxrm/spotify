from django.urls import path, include
from .views import GenreView, LicenseViewSets


urlpatterns = [
    path('genre/', GenreView.as_view()),

    path('license/', LicenseViewSets.as_view({'get': 'list', 'post': 'create'})),
    path('license/<int:pk>/', LicenseViewSets.as_view({'put': 'update', 'delete': 'destroy'})),
]