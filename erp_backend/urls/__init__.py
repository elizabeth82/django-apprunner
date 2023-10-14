from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from erp_backend.urls.versioned_urls import versioned_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt import views as jwt_views

API_PREFIX = getattr(settings, "API_PREFIX")
API_VERSION = getattr(settings, "API_VERSION")
DOCS_PREFIX = getattr(settings, "DOCS_PREFIX")
PLATFORM_PREFIX = getattr(settings, "PLATFORM_PREFIX")

admin_urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/", SpectacularAPIView.as_view(), name="schema"),  
    path(f"{API_PREFIX}/{API_VERSION}/", include(versioned_urls))
]

urlpatterns += admin_urlpatterns

# enable serve static by django or uwsgi

urlpatterns += static(
    getattr(settings, "STATIC_URL"),
    document_root=getattr(settings, "STATIC_ROOT"),
)

if getattr(settings, "DEBUG"):
    urlpatterns += static(
        getattr(settings, "MEDIA_URL"),
        document_root=getattr(settings, "MEDIA_ROOT"),
    )

# enable debug_toolbar for local develop (if installed)
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
