# -*- coding: utf-8 -*-

"""
Greeting List Class View
========================

Class-based view for listing and creating greetings.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
from ..models import Greeting, PERSISTENCE_ENABLED
from .helpers_api import get_client_ip, greeting_to_dict, parse_json_body


class GreetingListView(View):
    """
    Greeting List Class-Based View.

    Handle listing and creating greetings via class-based approach.
    """

    def get(self, request: HttpRequest) -> JsonResponse:
        """List all greetings."""
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
        """Create a new greeting."""
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
