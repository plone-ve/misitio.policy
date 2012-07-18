from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig
from plone.testing import z2

class MiSitioPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import misitio.policy
        xmlconfig.file('configure.zcml',
                       misitio.policy,
                       context=configurationContext)
        z2.installProduct(app, 'Products.CMFPlacefulWorkflow')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'misitio.policy:default')



FIXTURE = MiSitioPolicy()
INTEGRATION_TESTING = \
    IntegrationTesting(bases=(FIXTURE, ),
                       name="MiSitioPolicy:Integration")
