# -*- coding: utf-8 -*-
{
    'name': "Custom Invoices",

    'summary': """
        Custom Invoices Template.""",

    'description': """
        Customize invoice template for specific clients.
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Invoicing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_ext.xml',
        'views/report_action.xml',
        'views/custom_proforma1.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
