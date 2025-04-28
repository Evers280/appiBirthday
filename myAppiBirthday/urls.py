from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvitesViewSet, AdminViewSet, BilletsViewSet

router = DefaultRouter()
router.register(r'invites', InvitesViewSet, basename='invites')
router.register(r'admin', AdminViewSet, basename='admin')
router.register(r'billets', BilletsViewSet, basename='billeSts')

urlpatterns = [
    path('', include(router.urls)),
]


