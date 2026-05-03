# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Views Module
============

View functions and classes for the Swing Hello application.

This module consolidates all view components including function-based views,
class-based views, mixins, and helper utilities. Views are organized in
pairs (function and class implementations) for educational comparison.

View Categories
---------------

**Basic Response Views:**
    - :func:`hello_response_view` / :class:`HelloResponseView`: Plain text response.
    - :func:`hello_json_view` / :class:`HelloJsonView`: JSON response.
    - :func:`hello_template_view` / :class:`HelloTemplateView`: Template rendering.

**Form Views:**
    - :func:`hello_form_view` / :class:`HelloFormView`: Form handling.
    - :class:`FormHandlerMixin`: Reusable form logic mixin.

**API Views (with persistence):**
    - :func:`greeting_list_view` / :class:`GreetingListView`: List/create greetings.
    - :func:`greeting_detail_view` / :class:`GreetingDetailView`: Retrieve/delete greeting.

**API Views (stateless):**
    - :func:`greet_view` / :class:`GreetView`: Generate greeting without saving.

Helper Functions
----------------

- :func:`get_client_ip`: Extract client IP from request.
- :func:`parse_json_body`: Safely parse JSON from request body.
- :func:`generate_greeting`: Generate greeting message.
- :func:`greeting_to_dict`: Serialize Greeting model to dict.

Example:
    URL configuration::

        from swing.hello.views import (
            hello_response_view,
            HelloJsonView,
            GreetingListView,
        )

        urlpatterns = [
            path('hello/', hello_response_view),
            path('api/hello/', HelloJsonView.as_view()),
            path('api/greetings/', GreetingListView.as_view()),
        ]

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Local
# Import | Local Modules
from .helper_generate_greeting import generate_greeting
from .helper_get_client_ip import get_client_ip
from .helper_greeting_to_dict import greeting_to_dict
from .helper_parse_json_body import parse_json_body
from .mixin_form_handler import FormHandlerMixin
from .view_greet_class import GreetView
from .view_greet_func import greet_view
from .view_greeting_detail_class import GreetingDetailView
from .view_greeting_detail_func import greeting_detail_view
from .view_greeting_list_class import GreetingListView
from .view_greeting_list_func import greeting_list_view
from .view_hello_form_class import HelloFormView
from .view_hello_form_func import hello_form_view
from .view_hello_json_class import HelloJsonView
from .view_hello_json_func import hello_json_view
from .view_hello_response_class import HelloResponseView
from .view_hello_response_func import hello_response_view
from .view_hello_template_class import HelloTemplateView
from .view_hello_template_func import hello_template_view

# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "hello_response_view",
    "HelloResponseView",
    "hello_template_view",
    "HelloTemplateView",
    "hello_form_view",
    "HelloFormView",
    "hello_json_view",
    "HelloJsonView",
    "greeting_list_view",
    "greeting_detail_view",
    "greet_view",
    "GreetingListView",
    "GreetingDetailView",
    "GreetView",
    "FormHandlerMixin",
    "get_client_ip",
    "parse_json_body",
    "generate_greeting",
    "greeting_to_dict",
]
