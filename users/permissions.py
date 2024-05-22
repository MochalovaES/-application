from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        """Проверка на аутентификацию"""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Проверка на администратора"""
        return request.user.role == UserRoles.ADMIN


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        """Проверка на аутентификацию"""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Проверка на владельца"""
        return request.user.role == UserRoles.USER

