# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
API Views Tests Module
======================

This module contains tests for the API views in the Swing Hello application.
It tests both function-based and class-based API endpoints.

Classes:
--------
- TestGreetAPI: Tests for stateless greeting endpoint.
- TestGreetingListAPI: Tests for listing and creating greetings.
- TestGreetingDetailAPI: Tests for retrieving and deleting greetings.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import json
from typing import cast

from django.http import HttpResponse
from django.test import RequestFactory

# Import | Libraries
import pytest

# Import | Local
# Import | Local Modules
from ..models import Greeting, PERSISTENCE_ENABLED
from ..views.view_greet_class import GreetView
from ..views.view_greet_func import greet_view
from ..views.view_greeting_detail_class import GreetingDetailView
from ..views.view_greeting_detail_func import greeting_detail_view
from ..views.view_greeting_list_class import GreetingListView
from ..views.view_greeting_list_func import greeting_list_view

# =============================================================================
# Test Classes
# =============================================================================


class TestGreetAPI:
    """Tests for the stateless greet endpoint."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.factory = RequestFactory()

    def test_greet_valid_name(self) -> None:
        """Test greeting with valid name."""
        request = self.factory.post(
            "/hello/api/greet",
            data=json.dumps({"name": "John"}),
            content_type="application/json",
        )
        response = greet_view(request)

        assert response.status_code == 200
        data = json.loads(response.content)
        assert data["name"] == "John"
        assert "Hello" in data["message"]
        assert data["style"] == "casual"

    def test_greet_with_style(self) -> None:
        """Test greeting with specific style."""
        request = self.factory.post(
            "/hello/api/greet",
            data=json.dumps({"name": "John", "style": "formal"}),
            content_type="application/json",
        )
        response = greet_view(request)

        assert response.status_code == 200
        data = json.loads(response.content)
        assert "Good day" in data["message"]

    def test_greet_enthusiastic_style(self) -> None:
        """Test enthusiastic greeting style."""
        request = self.factory.post(
            "/hello/api/greet",
            data=json.dumps({"name": "John", "style": "enthusiastic"}),
            content_type="application/json",
        )
        response = greet_view(request)

        assert response.status_code == 200
        data = json.loads(response.content)
        assert "excited" in data["message"].lower()

    def test_greet_missing_name(self) -> None:
        """Test greeting without name returns error."""
        request = self.factory.post(
            "/hello/api/greet",
            data=json.dumps({}),
            content_type="application/json",
        )
        response = greet_view(request)

        assert response.status_code == 400
        data = json.loads(response.content)
        assert "error" in data

    def test_greet_empty_name(self) -> None:
        """Test greeting with empty name returns error."""
        request = self.factory.post(
            "/hello/api/greet",
            data=json.dumps({"name": ""}),
            content_type="application/json",
        )
        response = greet_view(request)

        assert response.status_code == 400

    def test_greet_invalid_name(self) -> None:
        """Test greeting with invalid name returns error."""
        request = self.factory.post(
            "/hello/api/greet",
            data=json.dumps({"name": "John123"}),
            content_type="application/json",
        )
        response = greet_view(request)

        assert response.status_code == 400

    def test_greet_cbv(self) -> None:
        """Test class-based greet view."""
        request = self.factory.post(
            "/hello/api/v2/greet",
            data=json.dumps({"name": "Jane"}),
            content_type="application/json",
        )
        response = cast(HttpResponse, GreetView.as_view()(request))

        assert response.status_code == 200
        data = json.loads(response.content)
        assert data["name"] == "Jane"


@pytest.mark.django_db
class TestGreetingListAPI:
    """Tests for the greeting list endpoint."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.factory = RequestFactory()

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_list_greetings_empty(self) -> None:
        """Test listing greetings when none exist."""
        Greeting.objects.all().delete()

        request = self.factory.get("/hello/api/greetings")
        response = greeting_list_view(request)

        assert response.status_code == 200
        data = json.loads(response.content)
        assert data["count"] == 0
        assert data["results"] == []

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_create_greeting(self) -> None:
        """Test creating a new greeting."""
        request = self.factory.post(
            "/hello/api/greetings",
            data=json.dumps({"name": "John", "style": "casual"}),
            content_type="application/json",
        )
        response = greeting_list_view(request)

        assert response.status_code == 201
        data = json.loads(response.content)
        assert data["name"] == "John"
        assert "id" in data

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_create_greeting_invalid_name(self) -> None:
        """Test creating greeting with invalid name fails."""
        request = self.factory.post(
            "/hello/api/greetings",
            data=json.dumps({"name": "John123"}),
            content_type="application/json",
        )
        response = greeting_list_view(request)

        assert response.status_code == 400

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_list_greetings_cbv(self) -> None:
        """Test class-based listing view."""
        request = self.factory.get("/hello/api/v2/greetings")
        response = GreetingListView.as_view()(request)

        assert response.status_code == 200


@pytest.mark.django_db
class TestGreetingDetailAPI:
    """Tests for the greeting detail endpoint."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.factory = RequestFactory()

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_get_greeting(self) -> None:
        """Test retrieving a specific greeting."""
        greeting = Greeting.create_greeting(name="John")

        request = self.factory.get(f"/hello/api/greetings/{greeting.pk}")
        response = greeting_detail_view(request, pk=greeting.pk)

        assert response.status_code == 200
        data = json.loads(response.content)
        assert data["name"] == "John"

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_get_greeting_not_found(self) -> None:
        """Test retrieving non-existent greeting returns 404."""
        request = self.factory.get("/hello/api/greetings/99999")
        response = greeting_detail_view(request, pk=99999)

        assert response.status_code == 404

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_delete_greeting(self) -> None:
        """Test deleting a greeting."""
        greeting = Greeting.create_greeting(name="John")
        pk = greeting.pk

        request = self.factory.delete(f"/hello/api/greetings/{pk}")
        response = greeting_detail_view(request, pk=pk)

        assert response.status_code == 204
        assert not Greeting.objects.filter(pk=pk).exists()

    @pytest.mark.skipif(
        not PERSISTENCE_ENABLED,
        reason="Persistence is disabled",
    )
    def test_detail_cbv(self) -> None:
        """Test class-based detail view."""
        greeting = Greeting.create_greeting(name="Jane")

        request = self.factory.get(f"/hello/api/v2/greetings/{greeting.pk}")
        response = GreetingDetailView.as_view()(request, pk=greeting.pk)

        assert response.status_code == 200


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "TestGreetAPI",
    "TestGreetingListAPI",
    "TestGreetingDetailAPI",
]
