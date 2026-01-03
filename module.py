"""
Example Module Configuration

This file defines the module metadata and navigation for the Example module.
Demonstrates how to create modules for ERPlora Hub with Ionic 8, Alpine.js and HTMX.
"""
from django.utils.translation import gettext_lazy as _

# Module Identification
MODULE_ID = "example"
MODULE_NAME = _("Example")
MODULE_DESCRIPTION = _("Functional example module demonstrating how to create modules for ERPlora Hub. Includes interactive examples with Ionic 8, Alpine.js and HTMX.")
MODULE_ICON = "code-slash-outline"
MODULE_VERSION = "0.2.0"
MODULE_AUTHOR = "ERPlora"
MODULE_CATEGORY = "utilities"
MODULE_COLOR = "tertiary"

# Target Industries (business verticals this module is designed for)
MODULE_INDUSTRIES = []  # Example module is for all industries

# Sidebar Menu Configuration
# This controls how the module appears in the main sidebar
MENU = {
    "label": _("Example"),
    "icon": "code-slash-outline",
    "order": 999,
    "show": True,
}

# Internal Navigation (Tabs)
# These are the tabs shown at the bottom when inside the module
NAVIGATION = [
    {
        "id": "dashboard",
        "label": _("Overview"),
        "icon": "home-outline",
        "view": "",  # Empty string for index/root
    },
    {
        "id": "components",
        "label": _("Components"),
        "icon": "cube-outline",
        "view": "components",
    },
    {
        "id": "forms",
        "label": _("Forms"),
        "icon": "create-outline",
        "view": "forms",
    },
    {
        "id": "htmx",
        "label": _("HTMX"),
        "icon": "flash-outline",
        "view": "htmx",
    },
]

# Module Dependencies
DEPENDENCIES = []

# Default Settings
SETTINGS = {}

# Permissions
# Format: (action_suffix, display_name) -> becomes "example.action_suffix"
PERMISSIONS = [
    ("view_examples", _("Can view examples")),
]

# Role Permissions - Default permissions for each system role in this module
ROLE_PERMISSIONS = {
    "admin": ["*"],
    "manager": ["view_examples"],
    "employee": ["view_examples"],
}
