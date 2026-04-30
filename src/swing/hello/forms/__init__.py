# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Hello Forms Module
==================

This module serves as the central point for importing and exporting all forms
used within the Swing Hello application. Currently, it includes the HelloForm
class, which is used to collect and validate a user's name.

Classes:
--------
- HelloForm: A form class for collecting and validating a user's name.

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Local
# Import | Local Modules
from .form_greeting import GreetingForm
from .form_hello import HelloForm
from .greeting_language import GreetingLanguage
from .greeting_style import GreetingStyle

# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "HelloForm",
    "GreetingForm",
    "GreetingStyle",
    "GreetingLanguage",
]
