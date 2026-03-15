from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# JWT va Swagger uchun kerakli kutubxonalar
from rest_framework import permissions # <-- Shuni qo'shing
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Chirchiq API",
        default_version='v1',
        description="Chirchiq shahri manzillari loyihasi uchun API hujjatlari",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,), # <-- Hammaga ko'rinishi uchun kerak
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # WEBSITE (HTML sahifalaringiz uchun)
    path('', include('manzil.urls')),

    # JWT AUTH (Login qilib token olish uchun)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # SWAGGER (Ustozingiz so'ragan chiroyli API ro'yxati)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Media fayllar (rasmlar) uchun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)