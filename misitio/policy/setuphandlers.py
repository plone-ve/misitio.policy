# -*- coding: utf-8 -*-

from misitio.policy.utils import createLink
from misitio.policy.utils import createDocument
from misitio.policy.utils import createFolder

def remove_default_content(site):
    """Borra el contenido creado en la instalacion de plone"""
    
    removable = ['Members','news','events','front-page']
    
    for item in removable:
        if hasattr(site, item):
            site.manage_delObjects([item])

def create_site_structure(site) :
    """Crea la estructura del sitio Misitio."""
    
    createFolder(site, u'Acerca de',
                 allowed_types=['Document','Folder'],
                 exclude_from_nav=False)
    
    createFolder(site, u'Contactos',
                 allowed_types=['Document','Folder','Image'],
                 exclude_from_nav=False)
    
    createFolder(site, u'Servicios',
                 allowed_types=['Document','Folder','Image','File'],
                 exclude_from_nav=False)
    
    createLink(site, u'Twitter', 'www.twitter.com/vtvcanal8', exclude_from_nav=False)
    
    createLink(site, u'Facebook', 'www.facebook.com/vtvcanal8', exclude_from_nav=False)
    
    createDocument(site['acerca-de'], u'Tu Compania')
    
    createDocument(site['acerca-de'], u'Ubicacion')
    
    createDocument(site['servicios'], u'Consultoria')
    
    createFolder(site['servicios'], u'Capacitacion',
                 allowed_types=['Document','Folder','Image','File'],
                 exclude_from_nav=False)
                 
    createDocument(site['servicios']['capacitacion'], u'Python')
    
    createDocument(site['servicios']['capacitacion'], u'Plone')

def setupVarious(context):
    """
    Metodo que ejecuta los pasos de personalizacion
    """
    
    if context.readDataFile('misitio.policy-default.txt') is None:
        return
        
    portal = context.getSite()
    remove_default_content(portal)
    create_site_structure(portal)
