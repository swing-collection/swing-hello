# -*- coding: utf-8 -*-

"""
Greeting List Function View
===========================

Function-based view for listing and creating greetings.
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
    Handle listing and creating greetings.

    GET: Returns a list of all greetings.
    POST: Creates a new greeting.

    Args:
        request: The HTTP request.

    Returns:
        JsonResponse with greeting data or error message.
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
