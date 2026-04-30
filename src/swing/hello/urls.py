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
from .views.view_greet_class import GreetView
from .views.view_greet_func import greet_view
from .views.view_greeting_detail_class import GreetingDetailView
from .views.view_greeting_detail_func import greeting_detail_view
from .views.view_greeting_list_class import GreetingListView
from .views.view_greeting_list_func import greeting_list_view
from .views.view_hello_form_class import HelloFormView
from .views.view_hello_form_func import hello_form_view
from .views.view_hello_json_class import HelloJsonView
from .views.view_hello_json_func import hello_json_view
from .views.view_hello_response_class import HelloResponseView
from .views.view_hello_response_func import hello_response_view
from .views.view_hello_template_class import HelloTemplateView
from .views.view_hello_template_func import hello_template_view

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
        route="response_func",
        view=hello_response_view,
        name="hello_response_func",
    ),
    path(
        route="template",
        view=HelloTemplateView.as_view(),
        name="hello_template",
    ),
    path(
        route="template_func",
        view=hello_template_view,
        name="hello_template_func",
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
