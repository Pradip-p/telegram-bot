from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', include('authentication.urls')),
    path('', include('bot.urls')),  
    path('admin/', admin.site.urls),
]
handler404 = "core.views.page_not_found_view"

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)