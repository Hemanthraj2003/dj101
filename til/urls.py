from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from feed import urls as feed_urls

urlpatterns = [
    path('god-mode/', admin.site.urls),
    path('',include(feed_urls, namespace="feed")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)