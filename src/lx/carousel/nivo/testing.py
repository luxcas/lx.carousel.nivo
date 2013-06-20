from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import lx.carousel.nivo


LX_CAROUSEL_NIVO = PloneWithPackageLayer(
    zcml_package=lx.carousel.nivo,
    zcml_filename='testing.zcml',
    name="LX_CAROUSEL_NIVO")

LX_CAROUSEL_NIVO_INTEGRATION = IntegrationTesting(
    bases=(LX_CAROUSEL_NIVO, ),
    name="LX_CAROUSEL_NIVO_INTEGRATION")

LX_CAROUSEL_NIVO_FUNCTIONAL = FunctionalTesting(
    bases=(LX_CAROUSEL_NIVO, ),
    name="LX_CAROUSEL_NIVO_FUNCTIONAL")
