from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
           and request.user.is_authenticated):
            return True
        return ((obj.author == request.user and request.user.is_staff)
                or request.user.is_superuser)
