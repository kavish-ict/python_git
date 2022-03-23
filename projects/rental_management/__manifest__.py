{
    'name': "Rental Management",

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
    'depends': ['base','sale_management','contacts'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',
        'views/rental.xml',
        'views/rental_type.xml',
        'views/product.xml',
        'views/sale.xml',
        'reports/report_1.xml',




    ],
    "license": "LGPL-3",
}

