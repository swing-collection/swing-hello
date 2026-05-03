# -*- coding: utf-8 -*-

"""
Hello Response Class View
=========================

A class-based view that returns a plain text "Hello!" response.

This module demonstrates Django's class-based view pattern using the
base ``View`` class. It provides the same functionality as the function-based
``hello_response_view`` but using object-oriented design.

Classes:
    HelloResponseView: CBV that returns a plain text greeting on GET.

Example:
    URL configuration::

        urlpatterns = [
            path('hello/', HelloResponseView.as_view(), name='hello'),
        ]

See Also:
    - :func:`hello_response_view`: Function-based equivalent.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext as _
from django.views import View


class HelloResponseView(View):
    """
    Class-based view returning a plain text "Hello!" response.

    A minimal class-based view demonstrating Django's CBV pattern.
    Handles GET requests and returns an internationalized greeting
    as plain text.

    This view serves as an educational example of the simplest possible
    class-based view implementation.

    Methods:
        get: Handle GET requests and return the greeting.

    Example:
        >>> view = HelloResponseView()
        >>> response = view.get(request)
        >>> response.content
        b'Hello!'

    See Also:
        - :func:`hello_response_view`: Function-based equivalent.
    """

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: dict[str, Any],
    ) -> HttpResponse:
        """
        Handles GET requests and returns a plain text "Hello!" response.

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


__all__: list[str] = ["HelloResponseView"]
