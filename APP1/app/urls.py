from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from app import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace='main')),
    path("catalog/", include("goods.urls", namespace='goods')),
    path("user/", include("users.urls", namespace='user')),
]

if settings.DEBUG:
    urlpatterns.extend([path("__debug__/", include("debug_toolbar.urls")), ])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
