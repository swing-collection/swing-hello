# -*- coding: utf-8 -*-

"""
Hello Form Class View
=====================

A class-based view that handles a simple form and renders a greeting message.
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
    Hello Form Class-Based View.

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


__all__: list[str] = ["HelloFormView"]
