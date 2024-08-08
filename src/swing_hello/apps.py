# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Hello Config Class
===========================

This module defines the configuration class for the 'hello' application within
the Django project. It specifies various attributes and settings for the app.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


# =============================================================================
# Classes
# =============================================================================

class HelloConfig(AppConfig):
    """
    Hello Config Class
    ==================
    
    Configuration class for the 'hello' application.

    """

    name = "hello"
    label = "hello"
    verbose_name = _("Hello World")
    default_auto_field = "django.db.models.BigAutoField"
