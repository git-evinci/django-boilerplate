"""Configuration for the Pages application.

This module contains the application configuration class for the Pages app,
used by Django to identify and manage the app.
"""
from django.apps import AppConfig


class PagesConfig(AppConfig):
    """Configuration class for the Pages app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "pages"
