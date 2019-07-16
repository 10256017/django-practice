from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view): #是否可看文章(針對model)
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # if request.user.is_authenticated and request.user.is_staff:
        #     return True
        # return False
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )

class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): #是否可看這一篇文章
        return  bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            (request.user == obj.creator or request.user == obj.staff)
        )
