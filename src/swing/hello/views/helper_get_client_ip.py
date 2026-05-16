# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Client IP Address Helper
========================

Utility function for extracting the client's IP address from HTTP requests.

This module handles both direct connections and requests proxied through
load balancers or reverse proxies by checking the ``X-Forwarded-For`` header.

Functions:
    get_client_ip: Extract client IP from Django HttpRequest.

Example:
    Using in a Django view::

        from swing.hello.views.helper_get_client_ip import get_client_ip

        def my_view(request):
            ip = get_client_ip(request)
            if ip:
                log.info(f"Request from {ip}")

Note:
    When behind a proxy, ensure ``X-Forwarded-For`` is properly configured
    to prevent IP spoofing.
"""

from django.http import HttpRequest


def get_client_ip(request: HttpRequest) -> str | None:
    """
    Extract the client's IP address from an HTTP request.

    Checks the ``X-Forwarded-For`` header first (for proxied requests),
    then falls back to ``REMOTE_ADDR``. For proxied requests, returns
    the first (original client) IP in the chain.

    Args:
        request: The Django HTTP request object.

    Returns:
        The client's IP address as a string, or None if not available.

    Example:
        >>> # Direct connection
        >>> request.META = {'REMOTE_ADDR': '192.168.1.1'}
        >>> get_client_ip(request)
        '192.168.1.1'

        >>> # Behind proxy
        >>> request.META = {'HTTP_X_FORWARDED_FOR': '1.2.3.4, 10.0.0.1'}
        >>> get_client_ip(request)
        '1.2.3.4'
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


__all__: list[str] = ["get_client_ip"]
