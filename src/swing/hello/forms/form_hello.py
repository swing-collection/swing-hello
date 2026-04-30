# -*- coding: utf-8 -*-

"""
Hello Form
==========

A basic form for collecting a user's name.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
            raise ValidationError(message=_("Name cannot be empty or only whitespace."))
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


__all__: list[str] = ["HelloForm"]
