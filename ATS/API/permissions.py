from rest_framework import permissions


class IsInterviewer(permissions.BasePermission):

    def has_permission(self, request, view):
        return hasattr('interviewer', 'request.user.interviewer')
