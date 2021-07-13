from constants.account_strings import AccountStrings
from rest_framework.permissions import BasePermission
from account.models import ParentProfile


class IsParent(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type != 3:
            return False
        return True
    message = AccountStrings.PermissionStrings.is_parent_message