# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting Detail Function View
=============================

Function-based API view for retrieving and deleting a specific greeting.

This module provides a RESTful endpoint for single Greeting resources,
supporting GET (retrieve) and DELETE operations.

Functions:
    greeting_detail_view: Handle retrieving/deleting a greeting.

Example:
    URL configuration::

        urlpatterns = [
            path('api/greetings/<int:pk>/', greeting_detail_view,
                 name='greeting_detail'),
        ]

See Also:
    - :class:`GreetingDetailView`: Class-based equivalent.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Import | Local
from ..models import Greeting, PERSISTENCE_ENABLED
from .helper_greeting_to_dict import greeting_to_dict


@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def greeting_detail_view(request: HttpRequest, pk: int) -> JsonResponse:
    """
    Handle retrieving and deleting a specific greeting.

    GET: Returns the greeting with the specified primary key.
    DELETE: Removes the greeting from the database.

    Args:
        request: The HTTP request (GET or DELETE).
        pk: The primary key of the greeting to operate on.

    Returns:
        JsonResponse containing:
            - On GET: The greeting data dict.
            - On DELETE: ``{"message": "Greeting deleted"}``
            - On error: ``{"error": "message"}``

    Status Codes:
        200: Greeting retrieved successfully.
        204: Greeting deleted successfully.
        404: Greeting not found.
        503: Persistence is disabled.

    Example:
        >>> response = greeting_detail_view(request, pk=1)
        >>> response.json()['name']
        'Alice'
    """
    if not PERSISTENCE_ENABLED:
        return JsonResponse(
            {"error": _("Persistence is disabled")},
            status=503,
        )

    try:
        greeting = Greeting.objects.get(pk=pk)
    except Greeting.DoesNotExist:
        return JsonResponse(
            {"error": _("Greeting not found")},
            status=404,
        )

    if request.method == "GET":
        return JsonResponse(greeting_to_dict(greeting))

    # DELETE
    greeting.delete()
    return JsonResponse(
        {"message": _("Greeting deleted")},
        status=204,
    )


__all__: list[str] = ["greeting_detail_view"]
