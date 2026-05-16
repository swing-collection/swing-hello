# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greet Function View
===================

Function-based view for stateless greeting generation.

This view generates greeting messages without persisting them to the
database. Useful for quick API responses where history is not needed.

Functions:
    greet_view: Generate a greeting message from POST data.

Example:
    URL configuration::

        urlpatterns = [
            path('api/greet/', greet_view, name='greet'),
        ]

    Request::

        POST /api/greet/
        Content-Type: application/json

        {"name": "Alice", "style": "formal"}

    Response::

        {"name": "Alice", "message": "Good day, Alice.", "style": "formal"}

See Also:
    - :class:`GreetView`: Class-based equivalent.
    - :func:`generate_greeting`: The greeting generation logic.
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
    Generate a greeting message without database persistence.

    Accepts JSON with a name and optional style, returns a generated
    greeting message. No data is saved to the database.

    Args:
        request: The HTTP POST request with JSON body containing:
            - name (str): The name to greet (required).
            - style (str): Greeting style, defaults to 'casual'.

    Returns:
        JsonResponse containing:
            - name: The input name.
            - message: The generated greeting.
            - style: The style used.

    Status Codes:
        200: Greeting generated successfully.
        400: Invalid data (missing/invalid name).

    Example:
        >>> response = greet_view(post_request)
        >>> response.json()
        {'name': 'Alice', 'message': 'Hey, Alice!', 'style': 'casual'}
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
