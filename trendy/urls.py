from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import default

urlpatterns = [
    path('', default),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('services/', include('services.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'trendy.views.error_404_view'