# -*- coding: utf-8 -*-
{
    'name': "Invoice Customization",

    'summary': """
        Customize built-in invoice.""",

    'description': """
        This module will customize customer invoices.
    """,

    'author': "Yaseen Malik",
    'website': "yaseenjamii666@gmail.com",
    'category': 'Accounting',
    'version': '0.1',

    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_invoice_ext.xml',
        'views/sale_order_ext.xml',
    ],
}
