# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Demo Settings for Swing Hello App
=================================

This is a basic settings configuration used to run the Swing Hello app 
in isolation. It includes minimal setup for a SQLite database, templates, 
and installed apps.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import os
from pathlib import Path

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Basic Configuration
# =============================================================================

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security: Use a strong secret key in production
SECRET_KEY = "django-insecure-change-this-in-production"

# Debug mode: Set to False in production
DEBUG = True

# Hosts allowed to access the application
ALLOWED_HOSTS = []


# =============================================================================
# Installed Applications
# =============================================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "swing_hello",
]
# =============================================================================
# Middleware
# =============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =============================================================================
# URL Configuration
# =============================================================================

ROOT_URLCONF = "demo.urls"


# =============================================================================
# Templates
# =============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Add paths to custom templates if needed
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =============================================================================
# WSGI Application
# =============================================================================

WSGI_APPLICATION = "demo.wsgi.application"


# =============================================================================
# Database
# =============================================================================

# SQLite database for development/testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}



# =============================================================================
# Password Validation
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =============================================================================
# Internationalization
# =============================================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# =============================================================================
# Static Files
# =============================================================================

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


# =============================================================================
# Default Primary Key Field Type
# =============================================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
