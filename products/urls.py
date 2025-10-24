from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ExternalPostSummaryViewSet, dashboard

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'external-posts', ExternalPostSummaryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', dashboard, name='dashboard'),
]
