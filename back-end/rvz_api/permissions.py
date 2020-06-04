from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # check if it's in the save methods
        if request.method in permissions.SAFE_METHODS:
            return True
        # otherwise, return the result of whether user is trying to update own profile
        return obj.id == request.user.id
