# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello JSON Class View
=====================

A class-based view that returns a JSON response with a greeting message.

This module demonstrates returning JSON data from a Django class-based
view. Extends Django's base ``View`` class and handles GET requests.

Classes:
    HelloJsonView: CBV that returns a JSON greeting.

Example:
    URL configuration::

        urlpatterns = [
            path('api/hello/', HelloJsonView.as_view(), name='hello_json'),
        ]

See Also:
    - :func:`hello_json_view`: Function-based equivalent.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View


class HelloJsonView(View):
    """
    Class-based view returning a JSON greeting response.

    Handles GET requests and returns a JSON object containing
    a greeting message. The message is internationalized using
    Django's translation system.

    Methods:
        get: Handle GET requests and return JSON response.

    Example:
        >>> view = HelloJsonView.as_view()
        >>> response = view(request)
        >>> response.json()
        {'message': 'Hello, World!'}
    """

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> JsonResponse:
        """
        Handle GET requests and return a JSON greeting.

        Args:
            request: The incoming HTTP request.
            *args: Variable positional arguments from URL pattern.
            **kwargs: Variable keyword arguments from URL pattern.

        Returns:
            A JsonResponse with ``{"message": "Hello, World!"}``.
        """
        data: dict[str, str] = {"message": _("Hello, World!")}
        return JsonResponse(data=data)


__all__: list[str] = ["HelloJsonView"]
