# -*- coding: utf-8 -*-

"""
Greeting Detail Class View
==========================

Class-based view for retrieving and deleting a specific greeting.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View

# Import | Local
from ..models import Greeting, PERSISTENCE_ENABLED
from .helpers_api import greeting_to_dict


class GreetingDetailView(View):
    """
    Greeting Detail Class-Based View.

    Handle retrieving and deleting a specific greeting.
    """

    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        """Retrieve a specific greeting."""
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
        """Delete a specific greeting."""
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
