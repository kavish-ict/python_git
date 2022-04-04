{
    'name': "Smart View",

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
    'depends': ['base','sale_management','contacts','hr','college_management'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',
        'data/category.xml',
        'data/ir_cron.xml',
        'views/sale_order.xml',
        'wizards/sale_order_wizard.xml',
        'wizards/sale_wizard.xml',
        'views/smart.xml',
        'views/res_settings.xml',
        'views/res_partner.xml',
        'views/smart_webpage.xml',
        'views/smart_formpage.xml'

    ],
    "license": "LGPL-3",
}
