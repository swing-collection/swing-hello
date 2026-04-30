# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Views Tests Module
========================

This module contains test cases for the views in the `swing_hello` application.
It includes function-based and class-based view tests for:

- HTTP response rendering
- Template rendering
- JSON responses
- Form processing

Test Classes:
-------------
- `TestHelloTemplateView`: Tests `hello_template_view` (FBV) and
    `HelloTemplateView` (CBV).

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from typing import Any

# Import | Libraries
import pytest
from django.http import HttpResponse
from django.http import HttpRequest
from django.test import RequestFactory
from django.utils.translation import gettext as _

# Import | Local Modules
from ..views.view_hello_template_class import HelloTemplateView
from ..views.view_hello_template_func import hello_template_view

# =============================================================================
# Test Classes
# =============================================================================


@pytest.mark.django_db
class TestHelloTemplateView:
    """
    TestHelloTemplateView
    =====================

    Test suite for the `hello_template_view` and `HelloTemplateView` views.

    This class includes tests for GET requests to ensure that the views render
    the correct template with the expected content.
    """

    def setup_method(self) -> None:
        """
        Setup Method
        ============

        Initializes the RequestFactory for use in test methods.

        The RequestFactory is used to simulate GET requests in the test
        methods.
        """
        self.factory: RequestFactory = RequestFactory()

    def test_hello_template_view_function(self) -> None:
        """
        Test hello_template_view Function (GET Request)
        ===============================================

        Tests GET request handling for the `hello_template_view`
        function-based view.

        Ensures that the function-based view renders the correct template
        and includes the expected content "Hello!" and "Lorem ipsum dolor
        sit amet".

        Assertions:
        -----------
        - The response status code should be 200 (OK).
        - The response content should include "Hello!" and "Lorem ipsum dolor
          sit amet".
        """
        request: HttpRequest = self.factory.get(path="/hello/template")
        response: HttpResponse = hello_template_view(request=request)

        assert response.status_code == 200
        assert _("Hello!") in response.content.decode()
        assert "Lorem ipsum dolor sit amet" in response.content.decode()

    def test_hello_template_view_class(self) -> None:
        """
        Test HelloTemplateView Class (GET Request)
        ==========================================

        Tests GET request handling for the `HelloTemplateView` class-based
        view.

        Ensures that the class-based view renders the correct template
        and includes the expected content "Hello!" and "Lorem ipsum dolor sit
        amet".

        Assertions:
        -----------
        - The response status code should be 200 (OK).
        - The response content should include "Hello!" and "Lorem ipsum dolor
        sit amet".
        """
        request: HttpRequest = self.factory.get("/hello/template")
        response: HttpResponse = HelloTemplateView.as_view()(request)

        assert response.status_code == 200
        assert _("Hello!") in response.content.decode()
        assert "Lorem ipsum dolor sit amet" in response.content.decode()


# =============================================================================
# Module Exports
# =============================================================================

__all__ = [
    "TestHelloTemplateView",
]
