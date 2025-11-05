from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, req, view):
        admin_permission = bool(req.user and req.user.is_staff)
        return req.method == 'GET' or admin_permission
    

class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, req, view, obj):
        if req.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == req.user or req.user.is_staff
        
