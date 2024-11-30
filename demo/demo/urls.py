# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import os

# Import | Libraries
from django.contrib import admin
from django.urls import path, include

# Import | Local Modules




urlpatterns = [
    path("admin/", admin.site.urls),  # Admin site URL
    path("hello/", include("swing_hello.urls")),  # Include the URLs from the swing_hello app
    path("", include("swing_hello.urls")),  # Include the URLs from the swing_hello app
]
