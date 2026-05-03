# -*- coding: utf-8 -*-

"""
Greeting Message Generator
==========================

Utility function for generating greeting messages without database persistence.

This module provides a stateless greeting generator that creates personalized
messages based on the recipient's name and chosen style. Messages are
internationalized using Django's translation system.

Functions:
    generate_greeting: Create a formatted greeting message.

Example:
    Basic usage::

        from swing.hello.views.helper_generate_greeting import generate_greeting

        message = generate_greeting("Alice", style="formal")
        # "Good day, Alice. It is a pleasure to meet you."

See Also:
    - :meth:`Greeting.create_greeting`: For persistent greetings.
    - :class:`GreetingStyle`: Available style constants.
"""

from django.utils.translation import gettext as _


def generate_greeting(name: str, style: str = "casual") -> str:
    """
    Generate a greeting message without persistence.

    Creates a personalized greeting based on the provided name and style.
    The message templates are translated using Django's i18n framework.

    Args:
        name: The name of the person to greet. Will be inserted into
            the message template.
        style: The greeting style to use. One of:
            - 'formal': Professional, respectful greeting.
            - 'casual': Friendly, everyday greeting (default).
            - 'enthusiastic': Excited, energetic greeting.

    Returns:
        The formatted greeting message string.

    Example:
        >>> generate_greeting("Bob")
        'Hello, Bob!'

        >>> generate_greeting("Alice", style="formal")
        'Good day, Alice. It is a pleasure to meet you.'

        >>> generate_greeting("Charlie", style="enthusiastic")
        'Hey Charlie! So excited to see you!'

    Note:
        Unknown styles fall back to 'casual'.
    """
    messages = {
        "formal": _("Good day, {name}. It is a pleasure to meet you."),
        "casual": _("Hello, {name}!"),
        "enthusiastic": _("Hey {name}! So excited to see you!"),
    }
    return messages.get(style, messages["casual"]).format(name=name)


__all__: list[str] = ["generate_greeting"]
