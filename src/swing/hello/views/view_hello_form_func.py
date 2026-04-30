# -*- coding: utf-8 -*-

"""
Hello Form Function View
========================

A function-based view that handles a simple form and returns a greeting message.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

# Import | Local
from ..forms import HelloForm


def hello_form_view(request: HttpRequest) -> HttpResponse:
    """
    A function-based view that handles a simple form. Renders a greeting
    message if the form is valid.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered HTML page with the form and greeting
            message.
    """
    if request.method == "POST":
        form = HelloForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            message: str = _("Hello, {name}!").format(name=name)
            return render(
                request=request,
                template_name="swing_hello/hello_form.html",
                context={
                    "form": form,
                    "message": message,
                },
            )
    else:
        form = HelloForm()

    return render(
        request=request,
        template_name="swing_hello/hello_form.html",
        context={"form": form},
    )


__all__: list[str] = ["hello_form_view"]
