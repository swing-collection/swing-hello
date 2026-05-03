# -*- coding: utf-8 -*-

"""
Hello Response Function View
============================

A simple function-based view that returns a plain text "Hello!" response.

This module demonstrates the most basic Django view pattern: a function
that takes an HttpRequest and returns an HttpResponse. The greeting text
is internationalized using Django's translation system.

Functions:
    hello_response_view: Return a plain text greeting.

Example:
    URL configuration::

        urlpatterns = [
            path('hello/', hello_response_view, name='hello'),
        ]

    Testing::

        >>> from django.test import RequestFactory
        >>> request = RequestFactory().get('/hello/')
        >>> response = hello_response_view(request)
        >>> response.content
        b'Hello!'

See Also:
    - :class:`HelloResponseView`: Class-based equivalent.
"""

from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext as _


def hello_response_view(request: HttpRequest) -> HttpResponse:
    """
    Return a plain text "Hello!" response.

    A minimal function-based view that demonstrates Django's basic
    request-response cycle. Returns a simple greeting as plain text.

    Args:
        request: The incoming HTTP request object. Not used directly
            but required by Django's view signature.

    Returns:
        An HttpResponse containing "Hello!" with content type text/plain.

    Example:
        >>> response = hello_response_view(request)
        >>> response.status_code
        200
        >>> response['Content-Type']
        'text/plain'
    """
    context: str = _("Hello!")
    return HttpResponse(
        content=context,
        content_type="text/plain",
    )


__all__: list[str] = ["hello_response_view"]
