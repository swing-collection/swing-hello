# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting Models Module
======================

This module defines the data models for the Swing Hello application,
providing optional persistence for greeting messages with full CRUD support.

The module supports both stateful (with database) and stateless deployments
through the ``SWING_HELLO_ENABLE_PERSISTENCE`` setting.

Classes:
    Greeting: Django model for storing greeting records with metadata.

Constants:
    PERSISTENCE_ENABLED: Boolean indicating if database persistence is active.

Example:
    Creating a greeting with persistence::

        from swing.hello.models import Greeting

        greeting = Greeting.create_greeting(
            name="Alice",
            style="formal",
            language="en",
        )
        print(greeting.message)  # "Good day, Alice. It is a pleasure..."

    Checking persistence status::

        from swing.hello.models import PERSISTENCE_ENABLED

        if PERSISTENCE_ENABLED:
            greetings = Greeting.objects.all()

Note:
    To disable persistence, add to your Django settings::

        SWING_HELLO_ENABLE_PERSISTENCE = False
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
    Greeting Model for storing greeting records.

    This model stores personalized greeting messages along with metadata
    such as the greeting style, language, creation timestamp, and optionally
    the requester's IP address.

    The model supports three greeting styles (formal, casual, enthusiastic)
    and can be extended to support additional languages through Django's
    internationalization framework.

    Attributes:
        name: The name of the person being greeted (max 100 chars).
        message: The generated greeting message (max 255 chars).
        style: The greeting style, one of 'formal', 'casual', 'enthusiastic'.
        language: The ISO 639-1 language code (e.g., 'en', 'nl', 'de').
        created_at: UTC timestamp when the greeting was created.
        ip_address: Optional IPv4/IPv6 address of the requester.

    Example:
        >>> greeting = Greeting.create_greeting(name="Bob", style="casual")
        >>> print(greeting)
        Bob: Hello, Bob!

    See Also:
        - :func:`create_greeting`: Factory method for creating greetings.
        - :class:`Style`: Enum of available greeting styles.
    """

    class Style(models.TextChoices):
        """Enumeration of greeting style choices.

        Defines the available styles for greeting messages:
            - FORMAL: Professional, respectful greeting.
            - CASUAL: Friendly, everyday greeting.
            - ENTHUSIASTIC: Excited, energetic greeting.
        """

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
        """Django model metadata configuration.

        Configures display names, default ordering, and database indexes
        for optimal query performance.
        """

        verbose_name = _("Greeting")
        verbose_name_plural = _("Greetings")
        ordering: ClassVar[list[str]] = ["-created_at"]
        indexes: ClassVar[list[models.Index]] = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self) -> str:
        """Return human-readable string representation.

        Returns:
            A string in the format "name: message".

        Example:
            >>> greeting = Greeting(name="Alice", message="Hello, Alice!")
            >>> str(greeting)
            'Alice: Hello, Alice!'
        """
        return f"{self.name}: {self.message}"

    def __repr__(self) -> str:
        """Return detailed developer-friendly representation.

        Returns:
            A string containing the model name and key attributes
            suitable for debugging.

        Example:
            >>> greeting = Greeting(pk=1, name="Alice", style="casual")
            >>> repr(greeting)
            "Greeting(id=1, name='Alice', style='casual', created_at=...)"
        """
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
        Factory method to create and persist a new greeting.

        Creates a personalized greeting message based on the specified style
        and saves it to the database. The message is automatically generated
        using Django's translation system for i18n support.

        Args:
            name: The name of the person to greet. Will appear in the
                generated message.
            style: The greeting style. Must be one of 'formal', 'casual',
                or 'enthusiastic'. Defaults to 'casual'.
            language: ISO 639-1 language code for the greeting.
                Defaults to 'en' (English).
            ip_address: Optional IPv4 or IPv6 address of the requester
                for analytics or logging purposes.

        Returns:
            A saved Greeting instance with the generated message.

        Raises:
            django.db.IntegrityError: If the greeting cannot be saved
                due to database constraints.

        Example:
            >>> greeting = Greeting.create_greeting(
            ...     name="Alice",
            ...     style="formal",
            ...     language="en",
            ...     ip_address="192.168.1.1"
            ... )
            >>> print(greeting.message)
            Good day, Alice. It is a pleasure to meet you.
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
