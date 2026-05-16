# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting Style Constants
========================

Defines the available greeting style choices for the Swing Hello application.

This module provides a simple container class with style constants and
choice tuples suitable for Django form fields and model fields.

Classes:
    GreetingStyle: Container for style constants and Django-compatible
        choice tuples.

Example:
    Using in a Django form field::

        style = forms.ChoiceField(
            choices=GreetingStyle.CHOICES,
            initial=GreetingStyle.CASUAL,
        )

See Also:
    - :class:`GreetingLanguage`: Language choices for greetings.
    - :class:`swing.hello.models.Greeting.Style`: Model-level style enum.
"""

from django.utils.translation import gettext_lazy as _


class GreetingStyle:
    """
    Container for greeting style constants and choices.

    Provides three greeting styles with different levels of formality:

    - **FORMAL**: Professional, respectful greetings suitable for
      business contexts.
    - **CASUAL**: Friendly, everyday greetings for general use.
    - **ENTHUSIASTIC**: Excited, energetic greetings for celebratory
      or informal contexts.

    Attributes:
        FORMAL: Constant 'formal' for professional greetings.
        CASUAL: Constant 'casual' for friendly greetings.
        ENTHUSIASTIC: Constant 'enthusiastic' for excited greetings.
        CHOICES: List of (value, label) tuples for Django form/model fields.
    """

    FORMAL = "formal"
    CASUAL = "casual"
    ENTHUSIASTIC = "enthusiastic"

    CHOICES = [
        (FORMAL, _("Formal")),
        (CASUAL, _("Casual")),
        (ENTHUSIASTIC, _("Enthusiastic")),
    ]


__all__: list[str] = ["GreetingStyle"]
