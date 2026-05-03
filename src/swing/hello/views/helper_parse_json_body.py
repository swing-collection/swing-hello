# -*- coding: utf-8 -*-

"""
JSON Request Body Parser
========================

Utility function for safely parsing JSON data from HTTP request bodies.

This module provides error-tolerant JSON parsing that gracefully handles
malformed JSON and encoding errors by returning an empty dictionary.

Functions:
    parse_json_body: Parse JSON from Django HttpRequest body.

Example:
    Using in an API view::

        from swing.hello.views.helper_parse_json_body import parse_json_body

        def api_view(request):
            data = parse_json_body(request)
            name = data.get('name', 'Anonymous')
            # ...

Note:
    This function silently handles parse errors. For strict parsing
    that raises exceptions, use ``json.loads()`` directly.
"""

# Import | Standard Library
import json
from typing import Any

from django.http import HttpRequest


def parse_json_body(request: HttpRequest) -> dict[str, Any]:
    """
    Safely parse JSON from an HTTP request body.

    Attempts to decode and parse the request body as JSON. If parsing
    fails due to invalid JSON or encoding issues, returns an empty
    dictionary instead of raising an exception.

    Args:
        request: The Django HTTP request containing JSON in its body.

    Returns:
        The parsed JSON as a dictionary, or an empty dict on parse error.

    Example:
        >>> # Valid JSON
        >>> request.body = b'{"name": "Alice"}'
        >>> parse_json_body(request)
        {'name': 'Alice'}

        >>> # Invalid JSON
        >>> request.body = b'not json'
        >>> parse_json_body(request)
        {}

    Warning:
        This function swallows parse errors silently. Validate the
        returned dict's contents for required fields.
    """
    try:
        return json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}


__all__: list[str] = ["parse_json_body"]
