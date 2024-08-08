# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Views Test Module
=======================

This module contains test classes for the views in the Swing Hello Django
application. It includes tests for both function-based and class-based views,
ensuring they return the expected responses and render the correct templates
with appropriate context.

Classes:
--------

- TestHelloResponseView: Tests for hello_response_view and HelloResponseView.
- TestHelloTemplateView: Tests for hello_template_view and HelloTemplateView.

Usage:
------

Run these tests using pytest to verify the functionality of the Swing
Hello views.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from typing import Any

# Import | Libraries
import pytest
from django.test import RequestFactory, HttpRequest, HttpResponse

# Import | Local
from swing_hello.views import (
    hello_response_view,
    HelloResponseView,
    hello_template_view,
    HelloTemplateView,
)


# =============================================================================
# Classes
# =============================================================================

@pytest.mark.django_db
class TestHelloResponseView:
    """
    Test suite for function-based and class-based response views.
    """

    def setup_method(self) -> None:
        """
        Set up the request factory for each test method.
        """
        self.factory: RequestFactory = RequestFactory()

    def test_hello_response_view_function(self) -> None:
        """
        Test the hello_response_view function-based view.
        """
        request: HttpRequest = self.factory.get('/hello/response')
        response: HttpResponse = hello_response_view(request)
        assert response.status_code == 200
        assert response.content.decode() == "Hello!"

    def test_hello_response_view_class(self) -> None:
        """
        Test the HelloResponseView class-based view.
        """
        request: HttpRequest = self.factory.get('/hello/response')
        response: HttpResponse = HelloResponseView.as_view()(request)
        assert response.status_code == 200
        assert response.content.decode() == "Hello!"


# =============================================================================

@pytest.mark.django_db
class TestHelloTemplateView:
    """
    Test suite for function-based and class-based template views.
    """

    def setup_method(self) -> None:
        """
        Set up the request factory for each test method.
        """
        self.factory: RequestFactory = RequestFactory()

    def test_hello_template_view_function(self) -> None:
        """
        Test the hello_template_view function-based view.
        """
        request: HttpRequest = self.factory.get('/hello/template')
        response: HttpResponse = hello_template_view(request)
        assert response.status_code == 200
        assert "Hello!" in response.content.decode()
        assert "Lorem ipsum dolor sit amet" in response.content.decode()

    def test_hello_template_view_class(self) -> None:
        """
        Test the HelloTemplateView class-based view.
        """
        request: HttpRequest = self.factory.get('/hello/template')
        response: HttpResponse = HelloTemplateView.as_view()(request)
        assert response.status_code == 200
        assert "Hello!" in response.content.decode()
        assert "Lorem ipsum dolor sit amet" in response.content.decode()


# =============================================================================
# Module Exports
# =============================================================================

__all__ = [
    "TestHelloResponseView",
    "TestHelloTemplateView",
]
