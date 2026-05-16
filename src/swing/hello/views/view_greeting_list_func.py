# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting List Function View
===========================

Function-based API view for listing and creating greetings.

This module provides a RESTful endpoint for the Greeting model,
supporting GET (list) and POST (create) operations with JSON
request/response format.

Functions:
    greeting_list_view: Handle listing and creating greetings.

Example:
    URL configuration::

        urlpatterns = [
            path('api/greetings/', greeting_list_view, name='greeting_list'),
        ]

    Creating a greeting::

        POST /api/greetings/
        Content-Type: application/json

        {"name": "Alice", "style": "formal", "language": "en"}

Note:
    This view is CSRF exempt and requires persistence to be enabled.

See Also:
    - :class:`GreetingListView`: Class-based equivalent.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Import | Local
from ..models import Greeting, PERSISTENCE_ENABLED
from .helper_get_client_ip import get_client_ip
from .helper_greeting_to_dict import greeting_to_dict
from .helper_parse_json_body import parse_json_body


@csrf_exempt
@require_http_methods(["GET", "POST"])
def greeting_list_view(request: HttpRequest) -> JsonResponse:
    """
    Handle listing and creating greetings via REST API.

    GET: Returns a list of up to 100 greetings.
    POST: Creates a new greeting from JSON data.

    Args:
        request: The HTTP request (GET or POST).

    Returns:
        JsonResponse containing:
            - On GET: ``{"count": N, "results": [...]}``
            - On POST success (201): Greeting data dict
            - On error: ``{"error": "message"}`` with appropriate status

    Status Codes:
        200: Successful list retrieval.
        201: Greeting created successfully.
        400: Invalid request data (missing/invalid name).
        503: Persistence is disabled.

    Example:
        >>> # List greetings
        >>> response = greeting_list_view(get_request)
        >>> response.json()['count']
        42
    """
    if not PERSISTENCE_ENABLED:
        return JsonResponse(
            {"error": _("Persistence is disabled")},
            status=503,
        )

    if request.method == "GET":
        greetings = Greeting.objects.all()[:100]
        return JsonResponse(
            {
                "count": greetings.count(),
                "results": [greeting_to_dict(g) for g in greetings],
            }
        )

    # POST
    data = parse_json_body(request)
    name = data.get("name", "").strip()

    if not name:
        return JsonResponse(
            {"error": _("Name is required")},
            status=400,
        )

    if not all(char.isalpha() or char.isspace() for char in name):
        return JsonResponse(
            {"error": _("Name should contain only letters and spaces")},
            status=400,
        )

    greeting = Greeting.create_greeting(
        name=name,
        style=data.get("style", "casual"),
        language=data.get("language", "en"),
        ip_address=get_client_ip(request),
    )

    return JsonResponse(
        greeting_to_dict(greeting),
        status=201,
    )


__all__: list[str] = ["greeting_list_view"]
