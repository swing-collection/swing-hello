# -*- coding: utf-8 -*-

"""
Parse JSON Body Helper
======================

Utility function to parse JSON from HTTP request body.
"""

# Import | Standard Library
import json
from typing import Any

from django.http import HttpRequest


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


__all__: list[str] = ["parse_json_body"]
