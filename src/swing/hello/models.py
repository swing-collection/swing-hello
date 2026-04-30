# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting Models Module
======================

This module defines the data models for the Swing Hello application.
The Greeting model provides optional persistence for greeting messages.

Models:
    - Greeting: Stores greeting records with name, message, and metadata.

Note:
    The model is optional for stateless deployments. Set
    `SWING_HELLO_ENABLE_PERSISTENCE = False` in Django settings to disable.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from typing import ClassVar

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# =============================================================================
# Configuration
# =============================================================================

PERSISTENCE_ENABLED = getattr(settings, "SWING_HELLO_ENABLE_PERSISTENCE", True)


# =============================================================================
# Models
# =============================================================================


class Greeting(models.Model):
    """
    Greeting Model
    ==============

    Stores greeting records with associated metadata.

    Attributes:
        name (str): The name of the person being greeted.
        message (str): The generated greeting message.
        style (str): The greeting style (formal, casual, enthusiastic).
        language (str): The language code used for the greeting.
        created_at (datetime): Timestamp when the greeting was created.
        ip_address (str | None): Optional IP address of the requester.

    """

    class Style(models.TextChoices):
        """Greeting style choices."""

        FORMAL = "formal", _("Formal")
        CASUAL = "casual", _("Casual")
        ENTHUSIASTIC = "enthusiastic", _("Enthusiastic")

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        help_text=_("The name of the person being greeted."),
    )

    message = models.CharField(
        verbose_name=_("Message"),
        max_length=255,
        help_text=_("The generated greeting message."),
    )

    style = models.CharField(
        verbose_name=_("Style"),
        max_length=20,
        choices=Style.choices,
        default=Style.CASUAL,
        help_text=_("The style of greeting."),
    )

    language = models.CharField(
        verbose_name=_("Language"),
        max_length=10,
        default="en",
        help_text=_("The language code for the greeting."),
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        default=timezone.now,
        help_text=_("When the greeting was created."),
    )

    ip_address = models.GenericIPAddressField(
        verbose_name=_("IP Address"),
        null=True,
        blank=True,
        help_text=_("IP address of the requester."),
    )

    class Meta:
        """Model metadata."""

        verbose_name = _("Greeting")
        verbose_name_plural = _("Greetings")
        ordering: ClassVar[list[str]] = ["-created_at"]
        indexes: ClassVar[list[models.Index]] = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self) -> str:
        """Return string representation."""
        return f"{self.name}: {self.message}"

    def __repr__(self) -> str:
        """Return detailed representation."""
        return (
            f"Greeting(id={self.pk}, name='{self.name}', "
            f"style='{self.style}', created_at={self.created_at})"
        )

    @classmethod
    def create_greeting(
        cls,
        name: str,
        style: str = "casual",
        language: str = "en",
        ip_address: str | None = None,
    ) -> "Greeting":
        """
        Create and save a new greeting.

        Args:
            name: The name to greet.
            style: Greeting style (formal, casual, enthusiastic).
            language: Language code for the greeting.
            ip_address: Optional IP address of the requester.

        Returns:
            The created Greeting instance.
        """
        from django.utils.translation import gettext as _

        messages = {
            "formal": _("Good day, {name}. It is a pleasure to meet you."),
            "casual": _("Hello, {name}!"),
            "enthusiastic": _("Hey {name}! So excited to see you!"),
        }

        message = messages.get(style, messages["casual"]).format(name=name)

        greeting = cls(
            name=name,
            message=message,
            style=style,
            language=language,
            ip_address=ip_address,
        )
        greeting.save()
        return greeting


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "Greeting",
    "PERSISTENCE_ENABLED",
]
