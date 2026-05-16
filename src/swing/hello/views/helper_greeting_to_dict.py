# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting Model Serializer
=========================

Utility function for converting Greeting model instances to dictionaries.

This module provides a simple serializer for the Greeting model, suitable
for JSON API responses. The output format is designed to be JSON-serializable
without additional processing.

Functions:
    greeting_to_dict: Convert a Greeting instance to a dictionary.

Example:
    In an API view::

        from swing.hello.views.helper_greeting_to_dict import greeting_to_dict
        from swing.hello.models import Greeting

        def greeting_detail(request, pk):
            greeting = Greeting.objects.get(pk=pk)
            return JsonResponse(greeting_to_dict(greeting))

Note:
    For bulk serialization, consider using Django REST Framework or
    list comprehensions with this function.
"""

# Import | Standard Library
from typing import Any

# Import | Local
from ..models import Greeting


def greeting_to_dict(greeting: Greeting) -> dict[str, Any]:
    """
    Convert a Greeting model instance to a JSON-serializable dictionary.

    Serializes all fields of a Greeting instance into a dictionary format
    suitable for JSON responses. Datetime fields are converted to ISO 8601
    format strings.

    Args:
        greeting: The Greeting model instance to serialize.

    Returns:
        A dictionary containing:
            - id (int): The greeting's primary key.
            - name (str): The name of the person greeted.
            - message (str): The generated greeting message.
            - style (str): The greeting style used.
            - language (str): The language code.
            - created_at (str): ISO 8601 formatted creation timestamp.
            - ip_address (str | None): The requester's IP address.

    Example:
        >>> greeting = Greeting(pk=1, name='Alice', message='Hello!')
        >>> greeting_to_dict(greeting)
        {'id': 1, 'name': 'Alice', 'message': 'Hello!', ...}
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


__all__: list[str] = ["greeting_to_dict"]
