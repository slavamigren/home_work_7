from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'Вы не модератор'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Вы не владелец'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsStudent(BasePermission):
    message = 'Вы не студент'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.STUDENT:
            return True
        return False


class IsStudentOwner(BasePermission):
    message = 'Вы не владелец'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False