# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
URL Configuration for Swing Hello
==================================

URL routing configuration for the swing.hello Django application.

This module defines all URL patterns, mapping HTTP endpoints to their
corresponding view functions and classes. URLs are organized into
categories for HTML views, form handling, and API endpoints.

URL Structure
-------------

**HTML Views (Template Rendering):**

- ``/`` - Default template view (HelloTemplateView)
- ``/response`` - Plain text response (CBV: HelloResponseView)
- ``/response_func`` - Plain text response (FBV: hello_response_view)
- ``/template`` - Template rendering (CBV: HelloTemplateView)
- ``/template_func`` - Template rendering (FBV: hello_template_view)
- ``/json`` - JSON response (CBV: HelloJsonView)
- ``/json_func`` - JSON response (FBV: hello_json_view)
- ``/form`` - Form handling (CBV: HelloFormView)
- ``/form_func`` - Form handling (FBV: hello_form_view)

**API v1 (Function-Based Views):**

- ``/api/greetings`` - List/create greetings (GET, POST)
- ``/api/greetings/<pk>`` - Retrieve/delete greeting (GET, DELETE)
- ``/api/greet`` - Generate stateless greeting (POST)

**API v2 (Class-Based Views):**

- ``/api/v2/greetings`` - List/create greetings (GET, POST)
- ``/api/v2/greetings/<pk>`` - Retrieve/delete greeting (GET, DELETE)
- ``/api/v2/greet`` - Generate stateless greeting (POST)

Example:
    Including in project URLconf::

        from django.urls import include, path

        urlpatterns = [
            path('hello/', include('swing.hello.urls')),
        ]

Note:
    Each endpoint has both function-based (FBV) and class-based (CBV)
    implementations for educational comparison.

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
