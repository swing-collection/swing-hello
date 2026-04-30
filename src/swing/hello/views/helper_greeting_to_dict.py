# -*- coding: utf-8 -*-

"""
Greeting to Dict Helper
=======================

Utility function to convert a Greeting model to a dictionary.
"""

# Import | Standard Library
from typing import Any

# Import | Local
from ..models import Greeting


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


__all__: list[str] = ["greeting_to_dict"]
