from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from navigation.api import Link, register_top_menu
from project_setup.api import register_setup
from project_tools.api import register_tool

from .conf.settings import SIDE_BAR_SEARCH, DISABLE_HOME_VIEW
from .utils import register_multi_items_links

__author__ = 'Roberto Rosario'
__copyright__ = 'Copyright 2011 Roberto Rosario'
__credits__ = ['Roberto Rosario', ]
__license__ = 'GPL'
__maintainer__ = 'Roberto Rosario'
__email__ = 'roberto.rosario.gonzalez@gmail.com'
__status__ = 'Production'

__version_info__ = {
    'major': 0,
    'minor': 13,
    'micro': 0,
    'releaselevel': 'alpha',
    'serial': 0
}


def is_superuser(context):
    return context['request'].user.is_staff or context['request'].user.is_superuser

maintenance_menu = Link(text=_(u'maintenance'), view='maintenance_menu', sprite='wrench', icon='wrench.png')
statistics = Link(text=_(u'statistics'), view='statistics', sprite='table', icon='blackboard_sum.png', condition=is_superuser, children_view_regex=[r'statistics'])
diagnostics = Link(text=_(u'diagnostics'), view='diagnostics', sprite='pill', icon='pill.png')
sentry = Link(text=_(u'sentry'), view='sentry', sprite='bug', icon='bug.png', condition=is_superuser)
admin_site = Link(text=_(u'admin site'), view='admin:index', sprite='keyboard', icon='keyboard.png', condition=is_superuser)

if not DISABLE_HOME_VIEW:
    register_top_menu('home', link=Link(text=_(u'home'), view='home', sprite='house'), position=0)
if not SIDE_BAR_SEARCH:
    register_top_menu('search', link=Link(text=_(u'search'), view='search', sprite='zoom', children_url_regex=[r'^search/']))


def get_version():
    '''
    Return the formatted version information
    '''
    vers = ['%(major)i.%(minor)i' % __version_info__, ]

    if __version_info__['micro']:
        vers.append('.%(micro)i' % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    register_setup(admin_site)

register_tool(maintenance_menu)
register_tool(statistics)
register_tool(diagnostics)

if 'sentry' in settings.INSTALLED_APPS:
    register_tool(sentry)

register_multi_items_links()