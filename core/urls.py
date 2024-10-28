from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.conf.urls.i18n import i18n_patterns

from .schema import swagger_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda _request: redirect('swagger/'), name='home'),
    
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("api/v1/user/", include("apps.user.urls", namespace="user")),
]


urlpatterns += i18n_patterns(
    path("api/v1/", include("apps.shop.urls", namespace="shop")),
    prefix_default_language = False,
)

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
