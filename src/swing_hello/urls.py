# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
URL Configuration
=================

Defines URL patterns for the Django application.

This module maps URLs to views, connecting web requests to the appropriate view 
logic.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
# (No standard library imports needed)

# Import | Libraries
from django.urls import path

# Import | Local Modules
from swing_hello.views.view_hello_response import HelloResponseView
from swing_hello.views.view_hello_template import HelloTemplateView


# =============================================================================
# URL Patterns
# =============================================================================

urlpatterns = [

    path(
        "",
        HelloTemplateView.as_view(),
        name="hello"
    ),

    path(
        "response",
        HelloResponseView.as_view(),
        name="hello_response"
    ),

    path(
        "template",
        HelloTemplateView.as_view(),
        name="hello_template"
    ),

]
