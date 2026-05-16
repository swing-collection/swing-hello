# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello JSON Function View
========================

A function-based view that returns a JSON response with a greeting message.

This module demonstrates returning JSON data from a Django view using
``JsonResponse``. The greeting message is internationalized.

Functions:
    hello_json_view: Return a JSON greeting response.

Example:
    URL configuration::

        urlpatterns = [
            path('api/hello/', hello_json_view, name='hello_json'),
        ]

    Response format::

        {"message": "Hello, World!"}

See Also:
    - :class:`HelloJsonView`: Class-based equivalent.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _


def hello_json_view(request: HttpRequest) -> JsonResponse:
    """
    Return a JSON response containing a greeting message.

    A simple API endpoint that returns a greeting in JSON format.
    The message is translated based on the active language.

    Args:
        request: The incoming HTTP request. The request method is
            not restricted but GET is the expected usage.

    Returns:
        A JsonResponse with ``{"message": "Hello, World!"}``.

    Example:
        >>> response = hello_json_view(request)
        >>> response.status_code
        200
        >>> response.json()
        {'message': 'Hello, World!'}
    """
    data: dict[str, str] = {"message": _("Hello, World!")}
    return JsonResponse(data=data)


__all__: list[str] = ["hello_json_view"]
