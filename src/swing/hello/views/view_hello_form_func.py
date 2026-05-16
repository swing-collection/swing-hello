# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Form Function View
========================

A function-based view for handling form submissions with a greeting response.

This module demonstrates Django form handling in a function-based view,
processing both GET (display empty form) and POST (process submission)
requests.

Functions:
    hello_form_view: Handle form display and submission.

Template:
    Uses ``swing_hello/hello_form.html``.

Example:
    URL configuration::

        urlpatterns = [
            path('hello/', hello_form_view, name='hello_form'),
        ]

See Also:
    - :class:`HelloFormView`: Class-based equivalent.
    - :class:`HelloForm`: The form class used.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

# Import | Local
from ..forms import HelloForm


def hello_form_view(request: HttpRequest) -> HttpResponse:
    """
    Handle form display and submission for a personalized greeting.

    On GET: Displays an empty HelloForm.
    On POST: Validates the form and, if valid, displays a personalized
    greeting message. Invalid forms are re-displayed with errors.

    Args:
        request: The incoming HTTP request (GET or POST).

    Returns:
        An HttpResponse with the rendered form template.

    Context:
        form: The HelloForm instance.
        message (optional): The greeting message if form was valid.

    Template:
        swing_hello/hello_form.html

    Example:
        >>> # POST with valid data
        >>> request = RequestFactory().post('/hello/', {'name': 'Alice'})
        >>> response = hello_form_view(request)
        >>> 'Hello, Alice!' in response.content.decode()
        True
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
