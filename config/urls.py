from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
      description="API на музыку на Django",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(url="https://t.me/deppkidd"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.oauth.urls')),
    path('audio/', include('src.audio_library.urls')),
]


swagger_url = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
    

urlpatterns = urlpatterns + swagger_url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)