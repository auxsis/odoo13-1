# -*- coding: utf-8 -*-
{
    'name': "Custom Pos Receipt",

    'summary': """
        Customized Pos Receipt""",

    'description': """
        Customized Pos Receipt"
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'POS',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos.xml',
        'views/pos_config.xml',
    ],
    'qweb': [
        'static/src/xml/pos_ticket_ext.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
