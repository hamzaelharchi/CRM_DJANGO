from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class ManagerRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is manager """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_manager:
            return redirect('products:product-list')
        return super().dispatch(request, *args, **kwargs)