# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Form Module
=================

This module defines form classes for collecting and validating user input
within the Swing Hello application.

Classes:
--------
- HelloForm: A basic form for collecting a user's name.
- GreetingForm: An extended form with style and language options.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from typing import Any

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Constants
# =============================================================================


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


# =============================================================================
# Forms
# =============================================================================


class HelloForm(forms.Form):
    """
    Hello Form Class
    ================

    A form for collecting a user's name.

    Fields:
    -------
    - name (str): A CharField for the user's name, limited to 100 characters.

    Methods:
    --------
    - clean_name() -> str: Custom validation method to ensure the name
      contains only alphabetic characters and spaces.
    - save() -> str: Placeholder method for saving form data.
    """

    name: forms.CharField = forms.CharField(
        label=_("Your Name"),
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter your name"),
                "class": "form-input",
                "autocomplete": "name",
            },
        ),
        help_text=_("Please enter your full name."),
    )

    def clean_name(self) -> str:
        """
        Custom validation for the 'name' field.

        Ensures that the name contains only alphabetic characters and spaces.

        Returns:
        --------
        - str: The cleaned name if valid.

        Raises:
        -------
        - ValidationError: If the name contains non-alphabetic characters.
        """
        name: str = self.cleaned_data.get("name", "")
        if not name.strip():
            raise ValidationError(
                message=_("Name cannot be empty or only whitespace.")
            )
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValidationError(
                message=_("Name should contain only letters and spaces.")
            )
        return name.strip()

    def save(self) -> str:
        """
        Placeholder for saving form data.

        Returns:
        --------
        - str: The cleaned name from the form.
        """
        return self.cleaned_data.get("name", "")


class GreetingForm(forms.Form):
    """
    Greeting Form Class
    ===================

    An extended form for creating greetings with style and language options.

    Fields:
    -------
    - name (str): The user's name.
    - style (str): The greeting style (formal, casual, enthusiastic).
    - language (str): The language for the greeting.

    Methods:
    --------
    - clean_name() -> str: Validates the name field.
    - get_greeting_message() -> str: Generates the greeting message.
    - save() -> dict: Returns the form data as a dictionary.
    """

    name = forms.CharField(
        label=_("Your Name"),
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter your name"),
                "class": "form-input",
                "autocomplete": "name",
            },
        ),
        help_text=_("Please enter your full name."),
    )

    style = forms.ChoiceField(
        label=_("Greeting Style"),
        choices=GreetingStyle.CHOICES,
        initial=GreetingStyle.CASUAL,
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
        ),
        help_text=_("Choose how you'd like to be greeted."),
    )

    language = forms.ChoiceField(
        label=_("Language"),
        choices=GreetingLanguage.CHOICES,
        initial=GreetingLanguage.ENGLISH,
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
        ),
        help_text=_("Choose the language for your greeting."),
    )

    def clean_name(self) -> str:
        """Validate the name field."""
        name: str = self.cleaned_data.get("name", "")
        if not name.strip():
            raise ValidationError(
                message=_("Name cannot be empty or only whitespace.")
            )
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValidationError(
                message=_("Name should contain only letters and spaces.")
            )
        return name.strip()

    def get_greeting_message(self) -> str:
        """
        Generate the greeting message based on form data.

        Returns:
        --------
        - str: The formatted greeting message.
        """
        from django.utils.translation import gettext as _

        name = self.cleaned_data.get("name", "")
        style = self.cleaned_data.get("style", GreetingStyle.CASUAL)

        messages = {
            GreetingStyle.FORMAL: _(
                "Good day, {name}. It is a pleasure to meet you."
            ),
            GreetingStyle.CASUAL: _("Hello, {name}!"),
            GreetingStyle.ENTHUSIASTIC: _(
                "Hey {name}! So excited to see you!"
            ),
        }

        template = messages.get(style, messages[GreetingStyle.CASUAL])
        return template.format(name=name)

    def save(self) -> dict[str, Any]:
        """
        Return form data as a dictionary.

        Returns:
        --------
        - dict: Form data including name, style, language, and message.
        """
        return {
            "name": self.cleaned_data.get("name", ""),
            "style": self.cleaned_data.get("style", GreetingStyle.CASUAL),
            "language": self.cleaned_data.get(
                "language", GreetingLanguage.ENGLISH
            ),
            "message": self.get_greeting_message(),
        }


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "HelloForm",
    "GreetingForm",
    "GreetingStyle",
    "GreetingLanguage",
]
