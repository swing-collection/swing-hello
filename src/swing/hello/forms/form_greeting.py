# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Greeting Form Module
====================

Provides an extended Django form for creating personalized greetings
with style and language options.

This module contains the ``GreetingForm`` class which extends the basic
name collection with additional fields for greeting style (formal, casual,
enthusiastic) and language selection.

Classes:
    GreetingForm: Full-featured form with name, style, and language fields.

Example:
    Creating a greeting with custom style::

        form = GreetingForm({
            'name': 'Alice',
            'style': 'formal',
            'language': 'en',
        })
        if form.is_valid():
            data = form.save()
            print(data['message'])
            # "Good day, Alice. It is a pleasure to meet you."

See Also:
    - :class:`HelloForm`: Simple form with name field only.
    - :class:`GreetingStyle`: Available greeting styles.
    - :class:`GreetingLanguage`: Available languages.
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
    Extended form for creating personalized greetings.

    This form collects a user's name along with optional style and language
    preferences to generate a customized greeting message. It supports
    three greeting styles and 12 languages.

    The form validates the name field and provides a ``get_greeting_message``
    method to generate the appropriate greeting based on the selected style.

    Attributes:
        name: CharField for the user's name (required, max 100 chars).
        style: ChoiceField for greeting style (optional, defaults to casual).
        language: ChoiceField for language (optional, defaults to English).

    Example:
        Basic usage::

            form = GreetingForm({
                'name': 'Bob',
                'style': 'enthusiastic',
            })
            if form.is_valid():
                print(form.get_greeting_message())
                # "Hey Bob! So excited to see you!"

        Getting all form data::

            data = form.save()
            # {'name': 'Bob', 'style': 'enthusiastic',
            #  'language': 'en', 'message': 'Hey Bob! ...'}

    See Also:
        - :class:`HelloForm`: Simple form with name only.
        - :class:`GreetingStyle`: Available style choices.
        - :class:`GreetingLanguage`: Available language choices.
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
        """
        Validate and clean the name field.

        Performs validation to ensure:
            - The name is not empty or whitespace-only.
            - The name contains only alphabetic characters and spaces.

        Returns:
            The cleaned and stripped name string.

        Raises:
            ValidationError: If validation fails.
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

    def get_greeting_message(self) -> str:
        """
        Generate a greeting message based on form data.

        Creates a personalized greeting using the cleaned name and selected
        style. The message template varies based on the style:

        - **formal**: "Good day, {name}. It is a pleasure to meet you."
        - **casual**: "Hello, {name}!"
        - **enthusiastic**: "Hey {name}! So excited to see you!"

        The returned message is translatable through Django's i18n system
        based on the active language.

        Returns:
            The formatted greeting message string.

        Note:
            This method should only be called after form validation
            (``is_valid()`` returns True).

        Example:
            >>> form = GreetingForm({'name': 'Alice', 'style': 'formal'})
            >>> form.is_valid()
            True
            >>> form.get_greeting_message()
            'Good day, Alice. It is a pleasure to meet you.'
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
        Return all form data including the generated message.

        Compiles the cleaned form data into a dictionary containing
        the name, style, language, and generated greeting message.

        Note:
            This does not persist to the database. To save a greeting,
            use :meth:`swing.hello.models.Greeting.create_greeting`.

        Returns:
            Dictionary containing:
                - name (str): The cleaned name.
                - style (str): The selected greeting style.
                - language (str): The selected language code.
                - message (str): The generated greeting message.

        Example:
            >>> form = GreetingForm({'name': 'Alice', 'style': 'casual'})
            >>> form.is_valid()
            True
            >>> form.save()
            {'name': 'Alice', 'style': 'casual', 'language': 'en',
             'message': 'Hello, Alice!'}
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
