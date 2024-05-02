# -*- coding: utf-8 -*-
{
    'name': 'Pragmatic Approve Hub',
    'version': '16.0.4',
    'category': 'Services',
    'author': 'Pragmatic TechSoft Pvt Ltd.',
    'website': 'http://pragtech.co.in',
    'summary': 'Pragmatic Approve Hub',
    'description': 'Pragmatic Approve Hub',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/approval_form.xml',
        'views/menu.xml',
        'data/approvehub_template.xml',
        'data/custom_approvehub_template.xml',
    ],
    'demo': ['demo/demo.xml'],
    'images': ['static/description/approve_hub_management_system.gif'],
    'live_test_url': 'http://www.pragtech.co.in/company/proposal-form.html?id=103&name=Pragmatic-Approve-Hub',
    'currency': 'USD',
    'price': 20,
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
}