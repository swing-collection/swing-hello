# -*- coding: utf-8 -*-

"""
Hello Template Function View
============================

A function-based view that renders a template with a given context.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _


def hello_template_view(request: HttpRequest) -> HttpResponse:
    """
    A function-based view that renders a template with a given context.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response object that renders the template
        with the provided context.
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
