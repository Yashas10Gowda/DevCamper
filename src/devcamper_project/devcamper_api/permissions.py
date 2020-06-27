from rest_framework import permissions


class UsersPermissions(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        return request.user.is_superuser


class BootcampsPermissions(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.publisher.id


class CoursesPermissions(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.instructor.id


class ReviewsPermissions(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        return True
