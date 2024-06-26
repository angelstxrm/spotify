from django.urls import path, include
from .views import UserProfileViewSet, AuthorView, SocialLinkViewSet


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('profile-me/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    
    path('author/', AuthorView.as_view({'get': 'list'})),
    path('author/<int:pk>/', AuthorView.as_view({'get': 'retrieve'})),

    path('social/', SocialLinkViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('social/<int:pk>/', SocialLinkViewSet.as_view({'put': 'update', 'delete': 'destroy'})),

]