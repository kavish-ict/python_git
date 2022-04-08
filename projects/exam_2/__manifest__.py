# -*- coding: utf-8 -*-
{
    'name': "Exam 2",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/exam.xml',
        'views/res_config.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'wizards/exam_wizard.xml',
        # 'wizards/saleorder_wizard.xml',

    ],
    'application':True,
    "license": "LGPL-3"
}
