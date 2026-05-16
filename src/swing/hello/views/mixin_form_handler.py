# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Form Handler Mixin
==================

A reusable mixin providing form handling logic for class-based views.

This module implements the common pattern of handling form display (GET)
and submission (POST) in Django views. Subclasses must implement the
``form_valid()`` method to define success behavior.

Classes:
    FormHandlerMixin: Mixin with GET/POST handlers for forms.

Example:
    Creating a form view::

        class MyFormView(FormHandlerMixin, View):
            form_class = MyForm
            template_name = 'my_form.html'

            def form_valid(self, form):
                # Process the valid form
                return redirect('success')

Note:
    This mixin must be used with a class that provides ``dispatch()``
    method, typically by inheriting from Django's ``View``.
"""

# Import | Standard Library
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Import | Local
from ..forms import HelloForm


class FormHandlerMixin:
    """
    Mixin providing reusable form handling for class-based views.

    Handles the common pattern of displaying a form on GET and
    processing submitted data on POST. Subclasses must implement
    ``form_valid()`` to define what happens when validation succeeds.

    Attributes:
        form_class: The form class to instantiate.
        template_name: Template path for rendering the form.
        success_url: Optional URL to redirect to on success.
        request: The current request (set by dispatch).

    Methods:
        dispatch: Store request and delegate to handler.
        get: Display empty form.
        post: Validate and process submitted form.
        form_valid: Handle valid form (must be implemented).

    Example:
        >>> class ContactView(FormHandlerMixin, View):
        ...     form_class = ContactForm
        ...     template_name = 'contact.html'
        ...     def form_valid(self, form):
        ...         form.save()
        ...         return redirect('thanks')
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
        """
        Store the request and delegate to the appropriate handler.

        This method captures the request for use by other methods
        and then calls the parent's dispatch method.

        Args:
            request: The incoming HTTP request.
            *args: Positional arguments from URL pattern.
            **kwargs: Keyword arguments from URL pattern.

        Returns:
            The response from the delegated handler method.
        """
        self.request = request
        return super().dispatch(request, *args, **kwargs)  # type: ignore[misc]

    def get(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        """
        Handle GET requests by displaying an empty form.

        Args:
            request: The incoming HTTP request.
            *args: Positional arguments from URL pattern.
            **kwargs: Keyword arguments from URL pattern.

        Returns:
            An HttpResponse with the rendered form template.

        Context:
            form: An unbound form instance.
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
        Handle POST requests by validating and processing form data.

        If the form is valid, delegates to ``form_valid()``. Otherwise,
        re-renders the template with the form containing errors.

        Args:
            request: The incoming HTTP request.
            *args: Positional arguments from URL pattern.
            **kwargs: Keyword arguments from URL pattern.

        Returns:
            An HttpResponse from form_valid() or re-rendered form.
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
        Process valid form data.

        Subclasses must override this method to define success behavior.
        Common implementations include saving data and redirecting.

        Args:
            form: The validated form instance.

        Returns:
            An HttpResponse (e.g., redirect or rendered template).

        Raises:
            NotImplementedError: If not overridden by subclass.
        """
        raise NotImplementedError("Subclasses must implement form_valid()")


__all__: list[str] = ["FormHandlerMixin"]
