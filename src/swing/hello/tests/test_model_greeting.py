# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Model Tests Module
==================

This module contains tests for the Greeting model in the Swing Hello
application.

Classes:
--------
- TestGreetingModel: Tests for the Greeting model.
"""

# =============================================================================
# Imports
# =============================================================================

from django.utils import timezone

# Import | Libraries
import pytest

# Import | Local
# Import | Local Modules
from ..models import Greeting, PERSISTENCE_ENABLED

# =============================================================================
# Test Classes
# =============================================================================


@pytest.mark.django_db
@pytest.mark.skipif(
    not PERSISTENCE_ENABLED,
    reason="Persistence is disabled",
)
class TestGreetingModel:
    """Tests for the Greeting model."""

    def test_create_greeting(self) -> None:
        """Test creating a greeting."""
        greeting = Greeting.create_greeting(name="John")

        assert greeting.pk is not None
        assert greeting.name == "John"
        assert "Hello" in greeting.message
        assert greeting.style == Greeting.Style.CASUAL

    def test_create_formal_greeting(self) -> None:
        """Test creating a formal greeting."""
        greeting = Greeting.create_greeting(
            name="John",
            style="formal",
        )

        assert "Good day" in greeting.message

    def test_create_enthusiastic_greeting(self) -> None:
        """Test creating an enthusiastic greeting."""
        greeting = Greeting.create_greeting(
            name="John",
            style="enthusiastic",
        )

        assert "excited" in greeting.message.lower()

    def test_greeting_with_language(self) -> None:
        """Test creating a greeting with language."""
        greeting = Greeting.create_greeting(
            name="John",
            language="nl",
        )

        assert greeting.language == "nl"

    def test_greeting_with_ip_address(self) -> None:
        """Test creating a greeting with IP address."""
        greeting = Greeting.create_greeting(
            name="John",
            ip_address="192.168.1.1",
        )

        assert greeting.ip_address == "192.168.1.1"

    def test_greeting_str(self) -> None:
        """Test string representation of greeting."""
        greeting = Greeting.create_greeting(name="John")

        assert "John" in str(greeting)
        assert "Hello" in str(greeting)

    def test_greeting_repr(self) -> None:
        """Test repr representation of greeting."""
        greeting = Greeting.create_greeting(name="John")

        repr_str = repr(greeting)
        assert "Greeting" in repr_str
        assert "John" in repr_str

    def test_greeting_ordering(self) -> None:
        """Test that greetings are ordered by created_at descending."""
        Greeting.objects.all().delete()

        g1 = Greeting.create_greeting(name="First")
        g2 = Greeting.create_greeting(name="Second")
        g3 = Greeting.create_greeting(name="Third")

        greetings = list(Greeting.objects.all())

        # Most recent first
        assert greetings[0].pk == g3.pk
        assert greetings[1].pk == g2.pk
        assert greetings[2].pk == g1.pk

    def test_greeting_created_at_auto(self) -> None:
        """Test that created_at is automatically set."""
        before = timezone.now()
        greeting = Greeting.create_greeting(name="John")
        after = timezone.now()

        assert before <= greeting.created_at <= after

    def test_greeting_style_choices(self) -> None:
        """Test greeting style choices."""
        assert Greeting.Style.FORMAL.value == "formal"
        assert Greeting.Style.CASUAL.value == "casual"
        assert Greeting.Style.ENTHUSIASTIC.value == "enthusiastic"

    def test_invalid_style_defaults_to_casual(self) -> None:
        """Test that invalid style defaults to casual message."""
        greeting = Greeting.create_greeting(
            name="John",
            style="invalid",
        )

        # Should use casual message as fallback
        assert "Hello" in greeting.message


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "TestGreetingModel",
]
