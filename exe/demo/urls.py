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

from django.contrib import admin
from django.urls import include, path
from django.urls.resolvers import URLResolver

# Import | Local Modules


# =============================================================================
# URL Patterns
# =============================================================================

urlpatterns: list[URLResolver] = [
    # Admin site URL
    path(
        route="admin/",
        view=admin.site.urls,
    ),
    # Include the URLs from the swing_hello app
    path(
        route="hello/",
        view=include(
            arg="swing.hello.urls",
        ),
    ),
    path(
        route="",
        view=include(
            arg="swing.hello.urls",
        ),
    ),
]
