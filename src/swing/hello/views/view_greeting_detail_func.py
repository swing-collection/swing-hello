# -*- coding: utf-8 -*-

"""
Greeting Detail Function View
=============================

Function-based view for retrieving and deleting a specific greeting.
"""

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Import | Local
from ..models import Greeting, PERSISTENCE_ENABLED
from .helpers_api import greeting_to_dict


@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def greeting_detail_view(request: HttpRequest, pk: int) -> JsonResponse:
    """
    Handle retrieving and deleting a specific greeting.

    GET: Returns the greeting with the given ID.
    DELETE: Deletes the greeting with the given ID.

    Args:
        request: The HTTP request.
        pk: The primary key of the greeting.

    Returns:
        JsonResponse with greeting data or error message.
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

    if request.method == "GET":
        return JsonResponse(greeting_to_dict(greeting))

    # DELETE
    greeting.delete()
    return JsonResponse(
        {"message": _("Greeting deleted")},
        status=204,
    )


__all__: list[str] = ["greeting_detail_view"]
