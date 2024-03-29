from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import robots_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('contact', include('contact.urls')),
    path('markdownx/', include('markdownx.urls')),
    path("updates/", include("updates.urls")),
    path("whatido/", include("whatido.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('robots.txt', robots_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
