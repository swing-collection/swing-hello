# -*- coding: utf-8 -*-

"""
Greet Function View
===================

Function-based view for stateless greeting generation.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Import | Local
from .helper_generate_greeting import generate_greeting
from .helper_parse_json_body import parse_json_body


@csrf_exempt
@require_http_methods(["POST"])
def greet_view(request: HttpRequest) -> JsonResponse:
    """
    Generate a greeting without persistence.

    POST: Generate a greeting message.

    Args:
        request: The HTTP request.

    Returns:
        JsonResponse with greeting message.
    """
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

    style = data.get("style", "casual")
    message = generate_greeting(name=name, style=style)

    return JsonResponse(
        {
            "name": name,
            "message": message,
            "style": style,
        }
    )


__all__: list[str] = ["greet_view"]
