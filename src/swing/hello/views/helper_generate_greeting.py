# -*- coding: utf-8 -*-

"""
Generate Greeting Helper
========================

Utility function to generate a greeting message without persistence.
"""

from django.utils.translation import gettext as _


def generate_greeting(name: str, style: str = "casual") -> str:
    """
    Generate a greeting message without persistence.

    Args:
        name: The name to greet.
        style: The greeting style (formal, casual, enthusiastic).

    Returns:
        The formatted greeting message.
    """
    messages = {
        "formal": _("Good day, {name}. It is a pleasure to meet you."),
        "casual": _("Hello, {name}!"),
        "enthusiastic": _("Hey {name}! So excited to see you!"),
    }
    return messages.get(style, messages["casual"]).format(name=name)


__all__: list[str] = ["generate_greeting"]
