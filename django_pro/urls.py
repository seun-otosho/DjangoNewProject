"""django_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    import debug_toolbar

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


if settings.SWAG:
    from wagtail.admin import urls as wagtailadmin_urls
    from wagtail.core import urls as wagtail_urls
    from wagtail.documents import urls as wagtaildocs_urls

    urlpatterns += [
        path('cms/', include(wagtailadmin_urls)),
        path('documents/', include(wagtaildocs_urls)),
        path('', include(wagtail_urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
