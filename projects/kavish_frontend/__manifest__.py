{
    'name': "Exam Frontend",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "KAVISH",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_recruitment', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/exam_frontend.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            "kavish_frontend/static/src/css/form.css"
        ]
    },
    "license": "LGPL-3"
}
# -*- coding: utf-8 -*-
