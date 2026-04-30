# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello API Views Module
======================

This module defines REST-style API views for the Swing Hello application.
All endpoints return JSON responses without requiring Django REST Framework.

Endpoints:
    - GET /api/greetings/ - List all greetings
    - POST /api/greetings/ - Create a new greeting
    - GET /api/greetings/{id}/ - Retrieve a specific greeting
    - DELETE /api/greetings/{id}/ - Delete a specific greeting
    - POST /api/greet/ - Stateless greeting (no persistence)

Functions:
    - greeting_list_view: List and create greetings
    - greeting_detail_view: Retrieve and delete a greeting
    - greet_view: Stateless greeting endpoint

Classes:
    - GreetingListView: CBV for listing and creating greetings
    - GreetingDetailView: CBV for retrieving and deleting a greeting
    - GreetView: CBV for stateless greeting
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import json
from typing import Any

from django.http import HttpRequest, HttpResponseNotAllowed, JsonResponse
from django.utils.translation import gettext as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Import | Local
# Import | Local Modules
from ..models import Greeting, PERSISTENCE_ENABLED

# =============================================================================
# Helper Functions
# =============================================================================


def get_client_ip(request: HttpRequest) -> str | None:
    """Extract client IP address from request."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def parse_json_body(request: HttpRequest) -> dict[str, Any]:
    """Parse JSON from request body."""
    try:
        return json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}


def generate_greeting(
    name: str,
    style: str = "casual",
) -> str:
    """Generate a greeting message without persistence."""
    messages = {
        "formal": _("Good day, {name}. It is a pleasure to meet you."),
        "casual": _("Hello, {name}!"),
        "enthusiastic": _("Hey {name}! So excited to see you!"),
    }
    return messages.get(style, messages["casual"]).format(name=name)


def greeting_to_dict(greeting: Greeting) -> dict[str, Any]:
    """Convert a Greeting model to a dictionary."""
    return {
        "id": greeting.pk,
        "name": greeting.name,
        "message": greeting.message,
        "style": greeting.style,
        "language": greeting.language,
        "created_at": greeting.created_at.isoformat(),
        "ip_address": greeting.ip_address,
    }


# =============================================================================
# Function-Based Views
# =============================================================================


@csrf_exempt
@require_http_methods(["GET", "POST"])
def greeting_list_view(request: HttpRequest) -> JsonResponse:
    """
    Greeting List View
    ==================

    Handle listing and creating greetings.

    GET: Returns a list of all greetings.
    POST: Creates a new greeting.

    Args:
        request: The HTTP request.

    Returns:
        JsonResponse with greeting data or error message.
    """
    if not PERSISTENCE_ENABLED:
        return JsonResponse(
            {"error": _("Persistence is disabled")},
            status=503,
        )

    if request.method == "GET":
        greetings = Greeting.objects.all()[:100]  # Limit to 100
        return JsonResponse(
            {
                "count": greetings.count(),
                "results": [greeting_to_dict(g) for g in greetings],
            }
        )

    # POST
    data = parse_json_body(request)
    name = data.get("name", "").strip()

    if not name:
        return JsonResponse(
            {"error": _("Name is required")},
            status=400,
        )

    if not all(char.isalpha() or char.isspace() for char in name):
        return JsonResponse(
            {"error": _("Name should contain only letters and spaces")},
            status=400,
        )

    greeting = Greeting.create_greeting(
        name=name,
        style=data.get("style", "casual"),
        language=data.get("language", "en"),
        ip_address=get_client_ip(request),
    )

    return JsonResponse(
        greeting_to_dict(greeting),
        status=201,
    )


@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def greeting_detail_view(request: HttpRequest, pk: int) -> JsonResponse:
    """
    Greeting Detail View
    ====================

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


@csrf_exempt
@require_http_methods(["POST"])
def greet_view(request: HttpRequest) -> JsonResponse:
    """
    Stateless Greet View
    ====================

    Generate a greeting without persistence.

    POST: Generate a greeting message.

    Args:
        request: The HTTP request.

    Returns:
        JsonResponse with greeting message.
    """
    data = parse_json_body(request)
    name = data.get("name", "").strip()

    if not name:
        return JsonResponse(
            {"error": _("Name is required")},
            status=400,
        )

    if not all(char.isalpha() or char.isspace() for char in name):
        return JsonResponse(
            {"error": _("Name should contain only letters and spaces")},
            status=400,
        )

    style = data.get("style", "casual")
    message = generate_greeting(name=name, style=style)

    return JsonResponse(
        {
            "name": name,
            "message": message,
            "style": style,
        }
    )


# =============================================================================
# Class-Based Views
# =============================================================================


class GreetingListView(View):
    """
    Greeting List Class-Based View
    ==============================

    Handle listing and creating greetings via class-based approach.
    """

    def get(self, request: HttpRequest) -> JsonResponse:
        """List all greetings."""
        if not PERSISTENCE_ENABLED:
            return JsonResponse(
                {"error": _("Persistence is disabled")},
                status=503,
            )

        greetings = Greeting.objects.all()[:100]
        return JsonResponse(
            {
                "count": greetings.count(),
                "results": [greeting_to_dict(g) for g in greetings],
            }
        )

    def post(self, request: HttpRequest) -> JsonResponse:
        """Create a new greeting."""
        if not PERSISTENCE_ENABLED:
            return JsonResponse(
                {"error": _("Persistence is disabled")},
                status=503,
            )

        data = parse_json_body(request)
        name = data.get("name", "").strip()

        if not name:
            return JsonResponse(
                {"error": _("Name is required")},
                status=400,
            )

        if not all(char.isalpha() or char.isspace() for char in name):
            return JsonResponse(
                {"error": _("Name should contain only letters and spaces")},
                status=400,
            )

        greeting = Greeting.create_greeting(
            name=name,
            style=data.get("style", "casual"),
            language=data.get("language", "en"),
            ip_address=get_client_ip(request),
        )

        return JsonResponse(
            greeting_to_dict(greeting),
            status=201,
        )


class GreetingDetailView(View):
    """
    Greeting Detail Class-Based View
    =================================

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


class GreetView(View):
    """
    Stateless Greet Class-Based View
    =================================

    Generate a greeting without persistence.
    """

    def post(self, request: HttpRequest) -> JsonResponse:
        """Generate a stateless greeting."""
        data = parse_json_body(request)
        name = data.get("name", "").strip()

        if not name:
            return JsonResponse(
                {"error": _("Name is required")},
                status=400,
            )

        if not all(char.isalpha() or char.isspace() for char in name):
            return JsonResponse(
                {"error": _("Name should contain only letters and spaces")},
                status=400,
            )

        style = data.get("style", "casual")
        message = generate_greeting(name=name, style=style)

        return JsonResponse(
            {
                "name": name,
                "message": message,
                "style": style,
            }
        )


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "greeting_list_view",
    "greeting_detail_view",
    "greet_view",
    "GreetingListView",
    "GreetingDetailView",
    "GreetView",
]
