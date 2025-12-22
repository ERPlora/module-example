"""
Tests básicos del plugin Example Plugin
"""

import pytest
from django.test import TestCase


class BasicTestCase(TestCase):
    """Tests básicos del plugin"""

    def test_plugin_loads(self):
        """Verifica que el plugin se carga correctamente"""
        from django.apps import apps
        app = apps.get_app_config('example')
        self.assertEqual(app.verbose_name, 'Example Plugin')
