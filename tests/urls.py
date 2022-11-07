import django
from django.urls import re_path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    re_path(r'^admin_resumable/', include('admin_async_upload.urls')),
    re_path(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        (r'^media/(?P<path>.*)$', django.views.static.serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
