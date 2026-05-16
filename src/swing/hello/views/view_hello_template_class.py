# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Template Class View
=========================

A class-based view that renders an HTML template with context data.

This module demonstrates Django's ``TemplateView`` generic class-based
view. It provides template rendering with custom context data.

Classes:
    HelloTemplateView: CBV that renders a hello template.

Template:
    Uses ``swing_hello/hello_template.html``.

Example:
    URL configuration::

        urlpatterns = [
            path('hello/', HelloTemplateView.as_view(), name='hello'),
        ]

See Also:
    - :func:`hello_template_view`: Function-based equivalent.
"""

# Import | Standard Library
from typing import Any

from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView


class HelloTemplateView(TemplateView):
    """
    Class-based view for rendering the hello template.

    Extends Django's ``TemplateView`` to render an HTML template with
    custom context data including a translated title and content.

    Attributes:
        template_name: Path to the template file.

    Methods:
        get_context_data: Add custom context for template rendering.

    Example:
        >>> view = HelloTemplateView.as_view()
        >>> response = view(request)
        >>> 'Hello!' in response.content.decode()
        True
    """

    template_name = "swing_hello/hello_template.html"

    def get_context_data(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Add custom context data for template rendering.

        Extends the base context with a translated title and content text.

        Args:
            **kwargs: Additional keyword arguments passed to the parent.

        Returns:
            Context dictionary with title and content keys added.

        Context:
            title: Translated "Hello!" string.
            content: Lorem ipsum placeholder text.
        """
        context: dict[str, Any] = super().get_context_data(**kwargs)
        context["title"] = _("Hello!")
        context["content"] = "Lorem ipsum dolor sit amet"
        return context


__all__: list[str] = ["HelloTemplateView"]
