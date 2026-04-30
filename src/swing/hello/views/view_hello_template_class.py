# -*- coding: utf-8 -*-

"""
Hello Template Class View
=========================

A class-based view that renders a template with a given context.
"""

# Import | Standard Library
from typing import Any

from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView


class HelloTemplateView(TemplateView):
    """
    A class-based view that renders a template with a given context.

    Attributes:
        template_name (str): The name of the template to be rendered.
    """

    template_name = "swing_hello/hello_template.html"

    def get_context_data(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Returns context for rendering the template.

        Parameters:
            **kwargs (dict[str, Any]): Arbitrary keyword arguments.

        Returns:
            dict: A dictionary containing context data for the template.
        """
        context: dict[str, Any] = super().get_context_data(**kwargs)
        context["title"] = _("Hello!")
        context["content"] = "Lorem ipsum dolor sit amet"
        return context


__all__: list[str] = ["HelloTemplateView"]
