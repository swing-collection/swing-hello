# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Form Views Module
=======================

This module defines views for handling a simple form that greets the user.
It includes both function-based and class-based views, with a reusable mixin
for handling form submissions. The views are equipped with internationalization
support to allow translation of messages into different languages.

Functions:
    - hello_form_view: A function-based view that handles a simple form
      and returns a greeting message.

Classes:
    - FormHandlerMixin: A reusable mixin for handling forms in class-based
      views.
    - HelloFormView: A class-based view that handles a simple form
      and returns a greeting message.

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
# Import | Local Modules
from ..forms.form_hello import HelloForm

# =============================================================================
# Functions
# =============================================================================


def hello_form_view(request: HttpRequest) -> HttpResponse:
    """
    Hello Form View Function
    ========================

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


# =============================================================================
# Classes
# =============================================================================


class FormHandlerMixin:
    """
    Form Handler Mixin
    ==================

    A reusable mixin for handling form submissions in class-based views.
    This mixin simplifies the process of managing forms, handling both GET
    and POST requests.

    Attributes:
        form_class (Type): The form class to be used in the view.
        template_name (str): The template name for rendering the form.
        success_url (str | None): The URL to redirect to after successful
            form submission.
    """

    form_class: type[HelloForm]
    template_name: str
    success_url: str | None = None
    request: HttpRequest  # Set by dispatch()

    def dispatch(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        """Store request and dispatch to appropriate handler."""
        self.request = request
        return super().dispatch(request, *args, **kwargs)  # type: ignore[misc]

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        """
        Handles GET requests to render the form.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The rendered HTML page with the form.
        """
        form: HelloForm = self.form_class()
        return render(
            request=request,
            template_name=self.template_name,
            context={"form": form},
        )

    def post(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        """
        Handles POST requests to process the form data.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The rendered HTML page with the form and any
                applicable messages, or redirects on success.
        """
        form: HelloForm = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form=form)
        return render(
            request=request,
            template_name=self.template_name,
            context={"form": form},
        )

    def form_valid(
        self,
        form: HelloForm,
    ) -> HttpResponse:
        """
        Processes valid form data. This method can be overridden by subclasses
        to provide custom form processing.

        Args:
            form (HelloForm): The valid form instance.

        Returns:
            HttpResponse: The rendered HTML page with a success message,
                or a redirect response.
        """
        raise NotImplementedError("Subclasses must implement form_valid()")


class HelloFormView(FormHandlerMixin, View):
    """
    Hello Form Class-Based View
    ===========================

    A class-based view that handles a simple form. Renders a greeting
    message if the form is valid.

    Inherits from:
        FormHandlerMixin: Reuses the form handling logic.
        View: Django's base view class.

    Attributes:
        form_class (type[HelloForm]): The form class to be used in the view.
        template_name (str): The template name for rendering the form.
    """

    form_class: type[HelloForm] = HelloForm
    template_name: str = "swing_hello/hello_form.html"

    def form_valid(
        self,
        form: HelloForm,
    ) -> HttpResponse:
        """
        Processes valid form data by rendering a greeting message.

        Args:
            form (HelloForm): The valid form instance.

        Returns:
            HttpResponse: The rendered HTML page with the greeting message.
        """
        name = form.cleaned_data["name"]
        message: str = _("Hello, {name}!").format(name=name)
        return render(
            request=self.request,
            template_name=self.template_name,
            context={"form": form, "message": message},
        )


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "hello_form_view",
    "FormHandlerMixin",
    "HelloFormView",
]
