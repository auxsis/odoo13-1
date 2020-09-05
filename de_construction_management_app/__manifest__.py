# -*- coding: utf-8 -*-
{
    'name': "Construction Management",

    'summary': """
        This module provide features to manage Construction Business / Industry.""",

    'description': """
        Construction Management of Construction Projects and Job Orders / Work Orders Management Odoo Module.
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    'category': 'Construction',
    'version': '0.0',

    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_task_ext.xml',
        'views/project_ext.xml',
        'views/material_requisition.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
