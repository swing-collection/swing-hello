# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Swing Hello Config Class
================================

This module defines the configuration class for the `swing_hello` application
within the Django project. It specifies metadata and settings used for
app registration.

"""


# =============================================================================
# Imports
# =============================================================================

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# =============================================================================
# Classes
# =============================================================================


class SwingHelloConfig(AppConfig):
    """
    Swing Hello Config Class
    ========================

    Defines settings and metadata for the `swing_hello` application.

    """

    name = "swing.hello"
    label = "swing_hello"
    verbose_name = _("Swing Hello")
    default_auto_field: str = "django.db.models.BigAutoField"
