# -*- coding: utf-8 -*-

"""
Hello JSON Class View
=====================

A class-based view that returns a JSON response with a greeting message.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View


class HelloJsonView(View):
    """
    Hello JSON Class-Based View.

    A class-based view that returns a JSON response with a greeting message.

    Inherits from:
        View: Django's base view class.
    """

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> JsonResponse:
        """
        Handles GET requests and returns a JSON response with a greeting
        message.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            JsonResponse: A JSON response containing the greeting message.
        """
        data: dict[str, str] = {"message": _("Hello, World!")}
        return JsonResponse(data=data)


__all__: list[str] = ["HelloJsonView"]
