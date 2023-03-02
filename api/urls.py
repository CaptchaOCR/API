from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .views import CaptchaViewSet

router = DefaultRouter()
router.register(r'captchas', CaptchaViewSet, basename='captcha')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
