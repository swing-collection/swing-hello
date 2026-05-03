# -*- coding: utf-8 -*-

"""
Greeting Detail Class View
==========================

Class-based API view for retrieving and deleting a specific greeting.

This module provides a RESTful endpoint using Django's class-based
view pattern for single Greeting resources.

Classes:
    GreetingDetailView: CBV for greeting retrieve/delete operations.

Example:
    URL configuration::

        urlpatterns = [
            path('api/greetings/<int:pk>/', GreetingDetailView.as_view(),
                 name='greeting_detail'),
        ]

See Also:
    - :func:`greeting_detail_view`: Function-based equivalent.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
from ..models import Greeting, PERSISTENCE_ENABLED
from .helper_greeting_to_dict import greeting_to_dict


class GreetingDetailView(View):
    """
    Class-based view for retrieving and deleting a specific greeting.

    Provides a REST API interface for individual Greeting instances
    with support for retrieval (GET) and deletion (DELETE).

    Methods:
        get: Retrieve a greeting by primary key.
        delete: Remove a greeting by primary key.

    Example:
        >>> view = GreetingDetailView.as_view()
        >>> response = view(request, pk=1)
    """

    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        """
        Retrieve a specific greeting by primary key.

        Args:
            request: The incoming HTTP request.
            pk: The primary key of the greeting to retrieve.

        Returns:
            JsonResponse with greeting data dict.

        Status Codes:
            200: Success.
            404: Greeting not found.
            503: Persistence is disabled.
        """
        if not PERSISTENCE_ENABLED:
            return JsonResponse(
                {"error": _("Persistence is disabled")},
                status=503,
            )

        try:
            greeting = Greeting.objects.get(pk=pk)
        except Greeting.DoesNotExist:
            return JsonResponse(
                {"error": _("Greeting not found")},
                status=404,
            )

        return JsonResponse(greeting_to_dict(greeting))

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        """
        Delete a specific greeting by primary key.

        Args:
            request: The incoming HTTP request.
            pk: The primary key of the greeting to delete.

        Returns:
            JsonResponse with deletion confirmation.

        Status Codes:
            204: Deleted successfully.
            404: Greeting not found.
            503: Persistence is disabled.
        """
        if not PERSISTENCE_ENABLED:
            return JsonResponse(
                {"error": _("Persistence is disabled")},
                status=503,
            )

        try:
            greeting = Greeting.objects.get(pk=pk)
        except Greeting.DoesNotExist:
            return JsonResponse(
                {"error": _("Greeting not found")},
                status=404,
            )

        greeting.delete()
        return JsonResponse(
            {"message": _("Greeting deleted")},
            status=204,
        )


__all__: list[str] = ["GreetingDetailView"]
