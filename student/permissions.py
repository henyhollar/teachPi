from rest_framework import permissions
from .views import get_mac_add, User


class MacAdd(permissions.BasePermission):
    
    message = 'You are not allowed to mark attendance for this course'

    def has_permission(self, request, view):
        
        mac_add = get_mac_add(request)
        user = User.objects.get(username=self.request.data['username'])
        if mac_add == user.mac_add:
            return True
        else:
            False
