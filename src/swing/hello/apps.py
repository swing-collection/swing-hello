# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django Application Configuration
================================

This module provides the Django application configuration for the
Swing Hello package. It registers the application with Django's
app registry and configures application-level metadata.

Classes:
    SwingHelloConfig: Django AppConfig subclass for swing.hello.

Configuration:
    The app uses 'swing.hello' as its Python path and 'swing_hello'
    as its label to avoid conflicts with other apps.

Usage:
    Add to INSTALLED_APPS in your Django settings::

        INSTALLED_APPS = [
            ...
            'swing.hello',
        ]

    Or with explicit config::

        INSTALLED_APPS = [
            ...
            'swing.hello.apps.SwingHelloConfig',
        ]
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
    Django application configuration for Swing Hello.

    This class configures the swing.hello application for use with Django's
    application registry. It provides metadata used by Django's admin site
    and application loading system.

    Attributes:
        name: Full Python path to the application ('swing.hello').
        label: Short unique identifier ('swing_hello') for database tables
            and admin references.
        verbose_name: Human-readable name for admin UI display.
        default_auto_field: Primary key field type for models.

    Note:
        The label uses underscores to ensure compatibility with Django's
        database table naming conventions.
    """

    name = "swing.hello"
    label = "swing_hello"
    verbose_name = _("Swing Hello")
    default_auto_field: str = "django.db.models.BigAutoField"
