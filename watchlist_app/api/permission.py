from rest_framework import permissions


class IsAdminORReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        admin = super().has_permission(request, view)  # return true if is admin
        return request.method == "GET" or admin


class IsOwnerORreadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):  # اشوف الموقع
        
        #obj الي بدي اعدل عليه 
        
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.review_user == request.user
