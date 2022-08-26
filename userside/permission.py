from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.usertype == "SuperAdmin" or(request.user.usertype == "Admin" and (request.method=='GET' or request.method=='PUT'))
        or (request.user.usertype == "User" and (request.method == 'GET')))