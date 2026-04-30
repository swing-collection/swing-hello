# -*- coding: utf-8 -*-

"""
Greet Class View
================

Class-based view for stateless greeting generation.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
from .helpers_api import generate_greeting, parse_json_body


class GreetView(View):
    """
    Stateless Greet Class-Based View.

    Generate a greeting without persistence.
    """

    def post(self, request: HttpRequest) -> JsonResponse:
        """Generate a stateless greeting."""
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
