from constants.general_strings import GeneralPermissionStrings
from rest_framework.permissions import BasePermission


class NotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated

    message = GeneralPermissionStrings.already_authenticated_message