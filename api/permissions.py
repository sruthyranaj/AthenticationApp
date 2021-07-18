from rest_framework import permissions

class IsPostOrIsAuthenticated(permissions.BasePermission):        
    
    def has_permission(self, request, view):
        """
        Method to restrict the api access.
        only post method is permitted.
        for accessing other methods user need to be login.
        """
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated