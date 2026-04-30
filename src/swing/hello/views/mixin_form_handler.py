# -*- coding: utf-8 -*-

"""
Form Handler Mixin
==================

A reusable mixin for handling form submissions in class-based views.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Import | Local
from ..forms import HelloForm


class FormHandlerMixin:
    """
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


__all__: list[str] = ["FormHandlerMixin"]
