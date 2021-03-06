# -*- coding: utf-8 -*-

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from misitio.policy.testing import INTEGRATION_TESTING
from misitio.policy.config import PROJECTNAME

class TestSetup(unittest.TestCase):

    layer = INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run 
        and the product installed
        """
        pid = PROJECTNAME
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed, 'package appears not to have been installed')
