from django.urls import path

from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Music API', permission_classes=(permissions.AllowAny,))

urlpatterns = [
   path('swagger/', schema_view),
]
