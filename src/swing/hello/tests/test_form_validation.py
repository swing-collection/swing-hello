# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Form Validation Tests Module
============================

This module contains tests for form validation in the Swing Hello application.
It tests both HelloForm and GreetingForm classes.

Classes:
--------
- TestHelloFormValidation: Tests for HelloForm validation logic.
- TestGreetingFormValidation: Tests for GreetingForm validation logic.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Libraries
import pytest

# Import | Local
# Import | Local Modules
from ..forms.form_hello import (
    GreetingForm,
    GreetingLanguage,
    GreetingStyle,
    HelloForm,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestHelloFormValidation:
    """Tests for HelloForm validation."""

    def test_valid_name(self) -> None:
        """Test that a valid name passes validation."""
        form = HelloForm(data={"name": "John Doe"})
        assert form.is_valid()
        assert form.cleaned_data["name"] == "John Doe"

    def test_valid_name_with_spaces(self) -> None:
        """Test that names with multiple spaces are valid."""
        form = HelloForm(data={"name": "John Michael Doe"})
        assert form.is_valid()
        assert form.cleaned_data["name"] == "John Michael Doe"

    def test_valid_unicode_name(self) -> None:
        """Test that unicode names are valid."""
        form = HelloForm(data={"name": "François Müller"})
        assert form.is_valid()

    def test_empty_name_invalid(self) -> None:
        """Test that empty name is invalid."""
        form = HelloForm(data={"name": ""})
        assert not form.is_valid()
        assert "name" in form.errors

    def test_whitespace_only_invalid(self) -> None:
        """Test that whitespace-only name is invalid."""
        form = HelloForm(data={"name": "   "})
        assert not form.is_valid()
        assert "name" in form.errors

    def test_name_with_numbers_invalid(self) -> None:
        """Test that names with numbers are invalid."""
        form = HelloForm(data={"name": "John123"})
        assert not form.is_valid()
        assert "name" in form.errors

    def test_name_with_special_chars_invalid(self) -> None:
        """Test that names with special characters are invalid."""
        form = HelloForm(data={"name": "John@Doe"})
        assert not form.is_valid()
        assert "name" in form.errors

    def test_name_with_hyphen_invalid(self) -> None:
        """Test that names with hyphens are invalid (strict validation)."""
        form = HelloForm(data={"name": "Mary-Jane"})
        assert not form.is_valid()

    def test_name_max_length(self) -> None:
        """Test that names exceeding max length are invalid."""
        long_name = "A" * 101
        form = HelloForm(data={"name": long_name})
        assert not form.is_valid()
        assert "name" in form.errors

    def test_name_at_max_length(self) -> None:
        """Test that names at exactly max length are valid."""
        name = "A" * 100
        form = HelloForm(data={"name": name})
        assert form.is_valid()

    def test_save_returns_name(self) -> None:
        """Test that save() returns the cleaned name."""
        form = HelloForm(data={"name": "John Doe"})
        assert form.is_valid()
        assert form.save() == "John Doe"

    def test_name_is_stripped(self) -> None:
        """Test that leading/trailing whitespace is stripped."""
        form = HelloForm(data={"name": "  John Doe  "})
        assert form.is_valid()
        assert form.cleaned_data["name"] == "John Doe"


class TestGreetingFormValidation:
    """Tests for GreetingForm validation."""

    def test_valid_greeting_form(self) -> None:
        """Test that a valid greeting form passes validation."""
        form = GreetingForm(
            data={
                "name": "John",
                "style": GreetingStyle.CASUAL,
                "language": GreetingLanguage.ENGLISH,
            }
        )
        assert form.is_valid()

    def test_default_style_and_language(self) -> None:
        """Test that style and language have defaults."""
        form = GreetingForm(data={"name": "John"})
        assert form.is_valid()
        # Defaults should be applied
        assert form.cleaned_data["style"] == GreetingStyle.CASUAL
        assert form.cleaned_data["language"] == GreetingLanguage.ENGLISH

    def test_formal_greeting_message(self) -> None:
        """Test formal greeting message generation."""
        form = GreetingForm(
            data={
                "name": "John",
                "style": GreetingStyle.FORMAL,
            }
        )
        assert form.is_valid()
        message = form.get_greeting_message()
        assert "Good day" in message
        assert "John" in message

    def test_casual_greeting_message(self) -> None:
        """Test casual greeting message generation."""
        form = GreetingForm(
            data={
                "name": "John",
                "style": GreetingStyle.CASUAL,
            }
        )
        assert form.is_valid()
        message = form.get_greeting_message()
        assert "Hello" in message
        assert "John" in message

    def test_enthusiastic_greeting_message(self) -> None:
        """Test enthusiastic greeting message generation."""
        form = GreetingForm(
            data={
                "name": "John",
                "style": GreetingStyle.ENTHUSIASTIC,
            }
        )
        assert form.is_valid()
        message = form.get_greeting_message()
        assert "excited" in message.lower()
        assert "John" in message

    def test_save_returns_dict(self) -> None:
        """Test that save() returns a dictionary with all fields."""
        form = GreetingForm(
            data={
                "name": "John",
                "style": GreetingStyle.FORMAL,
                "language": GreetingLanguage.DUTCH,
            }
        )
        assert form.is_valid()
        result = form.save()

        assert isinstance(result, dict)
        assert result["name"] == "John"
        assert result["style"] == GreetingStyle.FORMAL
        assert result["language"] == GreetingLanguage.DUTCH
        assert "message" in result

    def test_invalid_style_choice(self) -> None:
        """Test that invalid style choice is rejected."""
        form = GreetingForm(
            data={
                "name": "John",
                "style": "invalid_style",
            }
        )
        assert not form.is_valid()
        assert "style" in form.errors

    def test_invalid_language_choice(self) -> None:
        """Test that invalid language choice is rejected."""
        form = GreetingForm(
            data={
                "name": "John",
                "language": "xx",
            }
        )
        assert not form.is_valid()
        assert "language" in form.errors

    def test_name_validation_same_as_hello_form(self) -> None:
        """Test that name validation is consistent with HelloForm."""
        # Invalid name with numbers
        form = GreetingForm(data={"name": "John123"})
        assert not form.is_valid()
        assert "name" in form.errors


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "TestHelloFormValidation",
    "TestGreetingFormValidation",
]
