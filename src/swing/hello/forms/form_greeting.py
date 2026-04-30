# -*- coding: utf-8 -*-

"""
Greeting Form
=============

An extended form for creating greetings with style and language options.
"""

# Import | Standard Library
from typing import Any

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local
from .greeting_language import GreetingLanguage
from .greeting_style import GreetingStyle


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


__all__: list[str] = ["GreetingForm"]
