# -*- coding: utf-8 -*-
# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Resource Calendar',
    'version': '1.0',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'LGPL-3',
    'category': 'Others',
    'summary': 'resource calendar',
    'depends': [
        'calendar_resource',
        "resource",
        "calendar",
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'data/res_partner_timezone_admin.xml',
        'views/webclient_templates.xml',
        'views/room_type.xml',
        'views/resource.xml',
        'views/sector.xml',
        'views/room.xml',
        'views/instrument.xml',
    ],
    'installable': True,
    'application': True,
}
