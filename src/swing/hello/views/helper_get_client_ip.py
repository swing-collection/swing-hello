# -*- coding: utf-8 -*-

"""
Get Client IP Helper
====================

Utility function to extract client IP address from HTTP request.
"""

from django.http import HttpRequest


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


__all__: list[str] = ["get_client_ip"]
