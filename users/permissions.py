from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет владельцу объекта выполнять любые действия,
    а остальным пользователям — только чтение.
    """
    def has_object_permission(self, request, view, obj):
        """
        Проверяет, является ли пользователь владельцем объекта.
        """
        return (obj.author == request.user or request.method
                in permissions.SAFE_METHODS)


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет администратору выполнять любые действия,
    а остальным пользователям — только чтение.
    """
    def has_permission(self, request, view):
        """
        Проверяет, является ли пользователь администратором.
        """
        return (
                request.user.role == "admin" or request.method
                in permissions.SAFE_METHODS)
