# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting List Class View
========================

Class-based API view for listing and creating greetings.

This module provides a RESTful endpoint using Django's class-based
view pattern. Supports GET (list) and POST (create) operations.

Classes:
    GreetingListView: CBV for greeting list/create operations.

Example:
    URL configuration::

        urlpatterns = [
            path('api/greetings/', GreetingListView.as_view(),
                 name='greeting_list'),
        ]

See Also:
    - :func:`greeting_list_view`: Function-based equivalent.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
from ..models import Greeting, PERSISTENCE_ENABLED
from .helper_get_client_ip import get_client_ip
from .helper_greeting_to_dict import greeting_to_dict
from .helper_parse_json_body import parse_json_body


class GreetingListView(View):
    """
    Class-based view for listing and creating greetings.

    Provides a REST API interface for the Greeting model with
    support for listing (GET) and creation (POST) operations.

    Methods:
        get: List all greetings (up to 100).
        post: Create a new greeting from JSON data.

    Example:
        >>> view = GreetingListView.as_view()
        >>> response = view(request)  # Returns greeting list
    """

    def get(self, request: HttpRequest) -> JsonResponse:
        """
        List all greetings.

        Returns up to 100 greetings ordered by default queryset ordering.

        Args:
            request: The incoming HTTP request.

        Returns:
            JsonResponse with count and results array.

        Status Codes:
            200: Success.
            503: Persistence is disabled.
        """
        if not PERSISTENCE_ENABLED:
            return JsonResponse(
                {"error": _("Persistence is disabled")},
                status=503,
            )

        greetings = Greeting.objects.all()[:100]
        return JsonResponse(
            {
                "count": greetings.count(),
                "results": [greeting_to_dict(g) for g in greetings],
            }
        )

    def post(self, request: HttpRequest) -> JsonResponse:
        """
        Create a new greeting.

        Parses JSON from request body and creates a Greeting instance.
        Validates that name contains only letters and spaces.

        Args:
            request: The incoming HTTP request with JSON body.

        Returns:
            JsonResponse with created greeting data.

        Status Codes:
            201: Created successfully.
            400: Invalid data (missing/invalid name).
            503: Persistence is disabled.
        """
        if not PERSISTENCE_ENABLED:
            return JsonResponse(
                {"error": _("Persistence is disabled")},
                status=503,
            )

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


__all__: list[str] = ["GreetingListView"]
