# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from edu.iot.syllabus.interfaces import IUnit
from edu.iot.syllabus.testing import EDU_IOT_SYLLABUS_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class UnitIntegrationTest(unittest.TestCase):

    layer = EDU_IOT_SYLLABUS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Unit')
        schema = fti.lookupSchema()
        self.assertEqual(IUnit, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Unit')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Unit')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IUnit.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Unit',
            id='Unit',
        )
        self.assertTrue(IUnit.providedBy(obj))
