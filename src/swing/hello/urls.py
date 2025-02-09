# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
URL Configuration
=================

This module defines URL patterns for the `swing.hello` Django application.
It maps incoming HTTP requests to the appropriate views.


Available Endpoints:
--------------------
- `/`             → Renders the template with context
                    using `HelloTemplateView`.
- `/response/`    → Returns a plain text “Hello!” response
                    using `HelloResponseView`.
- `/template/`    → Renders the template with context
                    using `HelloTemplateView`.
- `/json/`        → Returns a JSON response using `HelloJsonView`.
- `/json_func/`   → Returns a JSON response using `hello_json_view`.
- `/form/`        → Displays a form and processes form submission
                    using `HelloFormView`.
- `/form_func/`   → Displays a form and processes form submission
                    using `hello_form_view`.
- `/api/`         → (Commented) A simple API endpoint returning a
                    JSON response using `HelloApiView`.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.urls import path
from django.urls.resolvers import URLPattern

# Import | Local Modules
from .views.view_hello_form import HelloFormView, hello_form_view
from .views.view_hello_json import HelloJsonView, hello_json_view
from .views.view_hello_response import HelloResponseView, hello_response_view
from .views.view_hello_template import HelloTemplateView, hello_template_view

# from .views.view_hello_api import HelloApiView

# =============================================================================
# URL Patterns
# =============================================================================

urlpatterns: list[URLPattern] = [
    path(
        route="",
        view=HelloTemplateView.as_view(),
        name="hello",
    ),
    path(
        route="response",
        view=HelloResponseView.as_view(),
        name="hello_response",
    ),
    path(
        route="template",
        view=HelloTemplateView.as_view(),
        name="hello_template",
    ),
    path(
        route="json",
        view=HelloJsonView.as_view(),
        name="hello_json",
    ),
    path(
        route="json_func",
        view=hello_json_view,
        name="hello_json_func",
    ),
    path(
        route="form",
        view=HelloFormView.as_view(),
        name="hello_form",
    ),
    path(
        route="form_func",
        view=hello_form_view,
        name="hello_form_func",
    ),
    # path(
    #     route="api",
    #     view=HelloApiView.as_view(),
    #     name="hello_api",
    # ),
]
