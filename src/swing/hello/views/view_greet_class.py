# -*- coding: utf-8 -*-

"""
Greet Class View
================

Class-based view for stateless greeting generation.

This view generates greeting messages without database persistence,
using Django's class-based view pattern.

Classes:
    GreetView: CBV for stateless greeting generation.

Example:
    URL configuration::

        urlpatterns = [
            path('api/greet/', GreetView.as_view(), name='greet'),
        ]

See Also:
    - :func:`greet_view`: Function-based equivalent.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
from .helper_generate_greeting import generate_greeting
from .helper_parse_json_body import parse_json_body


class GreetView(View):
    """
    Class-based view for stateless greeting generation.

    Generates greeting messages without saving to the database.
    Accepts POST requests with JSON containing name and optional style.

    Methods:
        post: Generate a greeting from JSON request data.

    Example:
        >>> view = GreetView.as_view()
        >>> response = view(request)
        >>> response.json()['message']
        'Hey, Alice!'
    """

    def post(self, request: HttpRequest) -> JsonResponse:
        """
        Generate a stateless greeting from POST data.

        Args:
            request: The HTTP POST request with JSON body.

        Returns:
            JsonResponse with name, message, and style.

        Status Codes:
            200: Greeting generated successfully.
            400: Invalid data (missing/invalid name).
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


__all__: list[str] = ["GreetView"]
