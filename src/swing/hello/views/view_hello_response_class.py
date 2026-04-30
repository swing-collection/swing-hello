# -*- coding: utf-8 -*-

"""
Hello Response Class View
=========================

A class-based view that returns a plain text "Hello!" response on GET request.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext as _
from django.views import View


class HelloResponseView(View):
    """
    A class-based view that returns a plain text "Hello!" response on a
    GET request.

    Methods:
        get(request, *args, **kwargs): Handles GET requests and returns
        "Hello!" text.
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
