from rest_framework import permissions
from .models import Admin


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        try:
            return request.user.admin.is_admin
        except Admin.DoesNotExist:
            return False