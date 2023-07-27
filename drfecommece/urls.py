from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from product.views import CategoryViewsSet


router= routers.DefaultRouter()
router.register(r"category", CategoryViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema', SpectacularAPIView.as_view(),name="schema"),
    path('api/schema/docs', SpectacularSwaggerView.as_view(url_name="schema"),),
]
