# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Template Function View
============================

A function-based view that renders an HTML template with context data.

This module demonstrates Django's template rendering using the ``render``
shortcut function. It provides a title and content to the template.

Functions:
    hello_template_view: Render the hello template with context.

Template:
    Uses ``swing_hello/hello_template.html`` which should display
    the title and content variables.

Example:
    URL configuration::

        urlpatterns = [
            path('hello/', hello_template_view, name='hello'),
        ]

See Also:
    - :class:`HelloTemplateView`: Class-based equivalent.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _


def hello_template_view(request: HttpRequest) -> HttpResponse:
    """
    Render the hello template with a title and content.

    Renders an HTML template with context containing a translated
    title and sample content text.

    Args:
        request: The incoming HTTP request.

    Returns:
        An HttpResponse with the rendered HTML template.

    Context:
        title: Translated "Hello!" string.
        content: Lorem ipsum placeholder text.

    Template:
        swing_hello/hello_template.html
    """
    context: dict[str, Any] = {
        "title": _("Hello!"),
        "content": "Lorem ipsum dolor sit amet",
    }
    return render(
        request=request,
        template_name="swing_hello/hello_template.html",
        context=context,
    )


__all__: list[str] = ["hello_template_view"]
