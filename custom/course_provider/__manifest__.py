# -*- coding: utf-8 -*-
{
    'name': "Open Academy Instructors",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "Makhmut",
    'website': "",
    'category': 'Productivity',
    'license': 'LGPL-3',
    'version': '0.1',
    'depends': [],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
