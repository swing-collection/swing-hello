# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting Language Constants
===========================

Defines the available language choices for greetings in the Swing Hello
application.

This module provides ISO 639-1 language codes and human-readable labels
for use in Django form fields and model fields. Supports 12 languages
including RTL languages (Arabic).

Classes:
    GreetingLanguage: Container for language constants and Django-compatible
        choice tuples.

Supported Languages:
    - English (en)
    - Dutch (nl)
    - German (de)
    - French (fr)
    - Spanish (es)
    - Italian (it)
    - Portuguese (pt)
    - Japanese (ja)
    - Chinese Simplified (zh_Hans)
    - Korean (ko)
    - Russian (ru)
    - Arabic (ar)

Example:
    Using in a Django form::

        language = forms.ChoiceField(
            choices=GreetingLanguage.CHOICES,
            initial=GreetingLanguage.ENGLISH,
        )
"""

from django.utils.translation import gettext_lazy as _


class GreetingLanguage:
    """
    Container for language code constants and choices.

    Provides ISO 639-1 language codes for all supported greeting languages.
    Labels are translatable using Django's internationalization framework.

    Attributes:
        ENGLISH: Language code 'en' for English.
        DUTCH: Language code 'nl' for Dutch.
        GERMAN: Language code 'de' for German.
        FRENCH: Language code 'fr' for French.
        SPANISH: Language code 'es' for Spanish.
        ITALIAN: Language code 'it' for Italian.
        PORTUGUESE: Language code 'pt' for Portuguese.
        JAPANESE: Language code 'ja' for Japanese.
        CHINESE: Language code 'zh_Hans' for Simplified Chinese.
        KOREAN: Language code 'ko' for Korean.
        RUSSIAN: Language code 'ru' for Russian.
        ARABIC: Language code 'ar' for Arabic.
        CHOICES: List of (code, label) tuples for form/model fields.
    """

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
