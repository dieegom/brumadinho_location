from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls', namespace='api')),
    path('', include('apps.map.urls', namespace='map')),
    path('', include('apps.missingpeople.urls', namespace='missingpeople'))

]
