# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edu.iot.syllabus


class EduIotSyllabusLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=edu.iot.syllabus)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edu.iot.syllabus:default')


EDU_IOT_SYLLABUS_FIXTURE = EduIotSyllabusLayer()


EDU_IOT_SYLLABUS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDU_IOT_SYLLABUS_FIXTURE,),
    name='EduIotSyllabusLayer:IntegrationTesting'
)


EDU_IOT_SYLLABUS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDU_IOT_SYLLABUS_FIXTURE,),
    name='EduIotSyllabusLayer:FunctionalTesting'
)


EDU_IOT_SYLLABUS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDU_IOT_SYLLABUS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EduIotSyllabusLayer:AcceptanceTesting'
)
