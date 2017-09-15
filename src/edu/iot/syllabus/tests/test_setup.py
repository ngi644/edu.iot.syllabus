# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from edu.iot.syllabus.testing import EDU_IOT_SYLLABUS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that edu.iot.syllabus is properly installed."""

    layer = EDU_IOT_SYLLABUS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edu.iot.syllabus is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edu.iot.syllabus'))

    def test_browserlayer(self):
        """Test that IEduIotSyllabusLayer is registered."""
        from edu.iot.syllabus.interfaces import (
            IEduIotSyllabusLayer)
        from plone.browserlayer import utils
        self.assertIn(IEduIotSyllabusLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDU_IOT_SYLLABUS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['edu.iot.syllabus'])

    def test_product_uninstalled(self):
        """Test if edu.iot.syllabus is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edu.iot.syllabus'))

    def test_browserlayer_removed(self):
        """Test that IEduIotSyllabusLayer is removed."""
        from edu.iot.syllabus.interfaces import \
            IEduIotSyllabusLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEduIotSyllabusLayer, utils.registered_layers())
