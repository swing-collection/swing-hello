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

from django.urls import path
from django.urls.resolvers import URLPattern

# Import | Local
# Import | Local Modules
from .views.view_hello_api import (
    greet_view,
    greeting_detail_view,
    greeting_list_view,
    GreetingDetailView,
    GreetingListView,
    GreetView,
)
from .views.view_hello_form import hello_form_view, HelloFormView
from .views.view_hello_json import hello_json_view, HelloJsonView
from .views.view_hello_response import hello_response_view, HelloResponseView
from .views.view_hello_template import hello_template_view, HelloTemplateView

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
    # API endpoints (function-based)
    path(
        route="api/greetings",
        view=greeting_list_view,
        name="api_greeting_list",
    ),
    path(
        route="api/greetings/<int:pk>",
        view=greeting_detail_view,
        name="api_greeting_detail",
    ),
    path(
        route="api/greet",
        view=greet_view,
        name="api_greet",
    ),
    # API endpoints (class-based)
    path(
        route="api/v2/greetings",
        view=GreetingListView.as_view(),
        name="api_v2_greeting_list",
    ),
    path(
        route="api/v2/greetings/<int:pk>",
        view=GreetingDetailView.as_view(),
        name="api_v2_greeting_detail",
    ),
    path(
        route="api/v2/greet",
        view=GreetView.as_view(),
        name="api_v2_greet",
    ),
]
