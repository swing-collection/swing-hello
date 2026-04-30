# -*- coding: utf-8 -*-

"""
Greeting Style
==============

Defines the available greeting style choices.
"""

from django.utils.translation import gettext_lazy as _


class GreetingStyle:
    """Greeting style choices."""

    FORMAL = "formal"
    CASUAL = "casual"
    ENTHUSIASTIC = "enthusiastic"

    CHOICES = [
        (FORMAL, _("Formal")),
        (CASUAL, _("Casual")),
        (ENTHUSIASTIC, _("Enthusiastic")),
    ]


__all__: list[str] = ["GreetingStyle"]
