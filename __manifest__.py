# -*- coding: utf-8 -*-
{
    'name': "accademy",

    'summary': "accademy module for register courses",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/academy_security.xml',
        'security/security_rules.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/partner.xml',
        'views/wizard.xml',
        'reports/session_report.xml',


    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

