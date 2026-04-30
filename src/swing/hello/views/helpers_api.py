# -*- coding: utf-8 -*-

"""
API Helper Functions
====================

Utility functions for API views in the Swing Hello application.
"""

# Import | Standard Library
import json
from typing import Any

from django.http import HttpRequest
from django.utils.translation import gettext as _

# Import | Local
from ..models import Greeting


def get_client_ip(request: HttpRequest) -> str | None:
    """
    Extract client IP address from request.

    Args:
        request: The HTTP request.

    Returns:
        The client IP address or None.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def parse_json_body(request: HttpRequest) -> dict[str, Any]:
    """
    Parse JSON from request body.

    Args:
        request: The HTTP request.

    Returns:
        Parsed JSON as dictionary, or empty dict on error.
    """
    try:
        return json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}


def generate_greeting(name: str, style: str = "casual") -> str:
    """
    Generate a greeting message without persistence.

    Args:
        name: The name to greet.
        style: The greeting style (formal, casual, enthusiastic).

    Returns:
        The formatted greeting message.
    """
    messages = {
        "formal": _("Good day, {name}. It is a pleasure to meet you."),
        "casual": _("Hello, {name}!"),
        "enthusiastic": _("Hey {name}! So excited to see you!"),
    }
    return messages.get(style, messages["casual"]).format(name=name)


def greeting_to_dict(greeting: Greeting) -> dict[str, Any]:
    """
    Convert a Greeting model to a dictionary.

    Args:
        greeting: The Greeting model instance.

    Returns:
        Dictionary representation of the greeting.
    """
    return {
        "id": greeting.pk,
        "name": greeting.name,
        "message": greeting.message,
        "style": greeting.style,
        "language": greeting.language,
        "created_at": greeting.created_at.isoformat(),
        "ip_address": greeting.ip_address,
    }


__all__: list[str] = [
    "get_client_ip",
    "parse_json_body",
    "generate_greeting",
    "greeting_to_dict",
]
