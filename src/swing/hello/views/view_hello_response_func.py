# -*- coding: utf-8 -*-

"""
Hello Response Function View
=============================

A simple function-based view that returns a plain text "Hello!" response.
"""

from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext as _


def hello_response_view(request: HttpRequest) -> HttpResponse:
    """
    A simple function-based view that returns a plain text "Hello!" response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response object with "Hello!" text.
    """
    context: str = _("Hello!")
    return HttpResponse(
        content=context,
        content_type="text/plain",
    )


__all__: list[str] = ["hello_response_view"]
