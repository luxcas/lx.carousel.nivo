===============================================
lx.carousel.nivo
===============================================

Overview
--------

This product is a installable Plone Theme developed by `Lucas
Aquino <http://www.lucasaquino.com.br/>`_.
 
Requirements
------------

    - Plone 3.2.x (http://plone.org/products/plone)
    
    - Plone 3.3.x (http://plone.org/products/plone)
    
    - Plone 4.x (http://plone.org/products/plone)

Installation
------------
    
To use this skin, on a buildout based installation:

    1. Unpack lx.carousel.nivo package to src/ folder of your 
    buildout
    2. Edit your buildout.cfg and add the following information::

        [buildout]
        ...
        eggs = 
            lx.carousel.nivo

        [instance]
        zcml = 
            ...
            lx.carousel.nivo
    
    The last line tells buildout to generate a zcml snippet that tells
    Zope to configure lx.carousel.nivo.

    If another package depends on the lx.carousel.nivo egg or 
    includes its zcml directly you do not need to specify anything in the 
    buildout configuration: buildout will detect this automatically.

    After updating the configuration you need to run the ''bin/buildout'',
    which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache to see the effects of the
product installation.

Browsers and OS's
-----------------
    * Internet Explorer 9.0 (WinXP/Vista)
    
    * Internet Explorer 8.0 (WinXP/Vista)
    
    * Internet Explorer 7.0 (WinXP/Vista)
    
    * Firefox 3 (WinXP/Vista/MacOSX)
    
    * Safari 4 (WinXP/Vista/MacOSX)
    
    * Safari 3 (WinXP/Vista/MacOSX)

Credits
-------

* Lucas Aquino (contato at lucasaquino dot com dot br) - Design / 
  Packaging

