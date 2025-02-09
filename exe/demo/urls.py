# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Demo URL Patterns
==========================

Defines URL patterns for the demo project. This includes:

- Admin panel routes for managing the application.
- Routes for the `swing_hello` app, including a default route.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.contrib import admin
from django.urls import include, path

# Import | Local Modules


# =============================================================================
# URL Patterns
# =============================================================================

urlpatterns = [
    path(
        route="admin/",
        view=admin.site.urls,
    ),  # Admin site URL
    path(
        route="hello/",
        view=include(
            arg="swing_hello.urls",
        ),
    ),  # Include the URLs from the swing_hello app
    path(
        route="",
        view=include(
            arg="swing_hello.urls",
        ),
    ),  # Include the URLs from the swing_hello app
]
