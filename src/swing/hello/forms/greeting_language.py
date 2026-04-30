# -*- coding: utf-8 -*-

"""
Greeting Language
=================

Defines the available language choices for greetings.
"""

from django.utils.translation import gettext_lazy as _


class GreetingLanguage:
    """Available language choices."""

    ENGLISH = "en"
    DUTCH = "nl"
    GERMAN = "de"
    FRENCH = "fr"
    SPANISH = "es"
    ITALIAN = "it"
    PORTUGUESE = "pt"
    JAPANESE = "ja"
    CHINESE = "zh_Hans"
    KOREAN = "ko"
    RUSSIAN = "ru"
    ARABIC = "ar"

    CHOICES = [
        (ENGLISH, _("English")),
        (DUTCH, _("Dutch")),
        (GERMAN, _("German")),
        (FRENCH, _("French")),
        (SPANISH, _("Spanish")),
        (ITALIAN, _("Italian")),
        (PORTUGUESE, _("Portuguese")),
        (JAPANESE, _("Japanese")),
        (CHINESE, _("Chinese")),
        (KOREAN, _("Korean")),
        (RUSSIAN, _("Russian")),
        (ARABIC, _("Arabic")),
    ]


__all__: list[str] = ["GreetingLanguage"]
