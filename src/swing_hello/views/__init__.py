# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Views Module
============

This module consolidates all view functions and classes used in the
application.

It imports the following views:
- hello_response_view (function-based view)
- HelloResponseView (class-based view)
- hello_template_view (function-based view)
- HelloTemplateView (class-based view)

These views demonstrate basic responses and template rendering in Django.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local Modules
from .view_hello_response import hello_response_view, HelloResponseView
from .view_hello_template import hello_template_view, HelloTemplateView


# =============================================================================
# Module Exports
# =============================================================================

__all__ = [
    "hello_response_view",
    "HelloResponseView",
    "hello_template_view",
    "HelloTemplateView",
]
