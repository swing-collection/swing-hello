# -*- coding: utf-8 -*-

"""
Hello JSON Function View
========================

A function-based view that returns a JSON response with a greeting message.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _


def hello_json_view(request: HttpRequest) -> JsonResponse:
    """
    A function-based view that returns a JSON response with a greeting message.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        JsonResponse: A JSON response containing the greeting message.
    """
    data: dict[str, str] = {"message": _("Hello, World!")}
    return JsonResponse(data=data)


__all__: list[str] = ["hello_json_view"]
