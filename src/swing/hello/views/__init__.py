# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Views Module
============

This module consolidates all view functions and classes used in the Swing Hello
application. It includes views for handling basic HTTP responses, rendering
templates, processing forms, and returning JSON responses.

Imported Views:
---------------

- hello_response_view (function-based view): Returns a basic HTTP response.
- HelloResponseView (class-based view): Returns a basic HTTP response.
- hello_template_view (function-based view): Renders a template with context.
- HelloTemplateView (class-based view): Renders a template with context.
- hello_form_view (function-based view): Handles form processing.
- HelloFormView (class-based view): Handles form processing.
- hello_json_view (function-based view): Returns a JSON response.
- HelloJsonView (class-based view): Returns a JSON response.

These views demonstrate basic responses, template rendering, form processing,
and JSON responses in Django.

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
