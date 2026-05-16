# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Form Module
=================

Provides a simple Django form for collecting and validating user names.

This module contains the basic ``HelloForm`` class used for simple greeting
interactions. For more advanced forms with style and language options,
see :mod:`swing.hello.forms.form_greeting`.

Classes:
    HelloForm: Basic form with name field and validation.

Example:
    Using in a Django view::

        def greet_view(request):
            if request.method == 'POST':
                form = HelloForm(request.POST)
                if form.is_valid():
                    name = form.cleaned_data['name']
                    return render(request, 'greeting.html', {'name': name})
            else:
                form = HelloForm()
            return render(request, 'form.html', {'form': form})

See Also:
    - :class:`GreetingForm`: Extended form with style/language options.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class HelloForm(forms.Form):
    """
    Simple form for collecting a user's name.

    This form provides a single text input field for the user's name with
    built-in validation to ensure the name contains only alphabetic
    characters and spaces.

    The form is suitable for basic greeting functionality where only a
    name is required. For forms with additional options like greeting
    style and language, use :class:`GreetingForm` instead.

    Attributes:
        name: CharField for the user's name (max 100 characters).

    Example:
        Basic usage::

            form = HelloForm({'name': 'Alice'})
            if form.is_valid():
                print(f"Hello, {form.cleaned_data['name']}!")

        With validation error::

            form = HelloForm({'name': 'Alice123'})  # Contains numbers
            form.is_valid()  # Returns False
            print(form.errors['name'])  # Validation error message
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
        Validate and clean the name field.

        Performs validation to ensure:
            - The name is not empty or whitespace-only.
            - The name contains only alphabetic characters and spaces.

        Returns:
            The cleaned and stripped name string.

        Raises:
            ValidationError: If the name is empty, whitespace-only,
                or contains non-alphabetic characters.

        Example:
            >>> form = HelloForm({'name': '  Alice  '})
            >>> form.is_valid()
            True
            >>> form.cleaned_data['name']
            'Alice'
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
        Return the validated name from the form.

        This is a convenience method that retrieves the cleaned name.
        Note that this does not persist data to the database; use
        :meth:`swing.hello.models.Greeting.create_greeting` for that.

        Returns:
            The cleaned name string from the form data.

        Example:
            >>> form = HelloForm({'name': 'Alice'})
            >>> if form.is_valid():
            ...     name = form.save()
            ...     print(f"Hello, {name}!")
            Hello, Alice!
        """
        return self.cleaned_data.get("name", "")


__all__: list[str] = ["HelloForm"]
