# -*- coding: utf-8 -*-

"""
Hello Form Class View
=====================

A class-based view for handling form submissions with a greeting response.

This module demonstrates Django form handling using a class-based view
with a reusable mixin. It provides the same functionality as the
function-based ``hello_form_view``.

Classes:
    HelloFormView: CBV for handling HelloForm submissions.

Template:
    Uses ``swing_hello/hello_form.html``.

Example:
    URL configuration::

        urlpatterns = [
            path('hello/', HelloFormView.as_view(), name='hello_form'),
        ]

See Also:
    - :func:`hello_form_view`: Function-based equivalent.
    - :class:`FormHandlerMixin`: The mixin providing form logic.
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
from ..forms import HelloForm
from .mixin_form_handler import FormHandlerMixin


class HelloFormView(FormHandlerMixin, View):
    """
    Class-based view for handling form submissions with greetings.

    Combines ``FormHandlerMixin`` with Django's ``View`` to handle form
    display and processing. Overrides ``form_valid()`` to generate
    a personalized greeting.

    Attributes:
        form_class: The form class to instantiate (HelloForm).
        template_name: Path to the form template.

    Methods:
        form_valid: Process valid form data and generate greeting.

    Example:
        >>> view = HelloFormView.as_view()
        >>> response = view(request)  # GET shows empty form
    """

    form_class: type[HelloForm] = HelloForm
    template_name: str = "swing_hello/hello_form.html"

    def form_valid(
        self,
        form: HelloForm,
    ) -> HttpResponse:
        """
        Process valid form data and render a personalized greeting.

        Called by the mixin when form validation succeeds. Extracts
        the name from cleaned data and generates a greeting message.

        Args:
            form: The validated HelloForm instance.

        Returns:
            An HttpResponse with the template showing the greeting.

        Context:
            form: The validated form instance.
            message: The personalized greeting string.
        """
        name = form.cleaned_data["name"]
        message: str = _("Hello, {name}!").format(name=name)
        return render(
            request=self.request,
            template_name=self.template_name,
            context={"form": form, "message": message},
        )


__all__: list[str] = ["HelloFormView"]
