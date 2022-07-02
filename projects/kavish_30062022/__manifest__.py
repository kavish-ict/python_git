{
    'name': 'Backend Task',
    'summary': """Displaying Covid Message""",
    'description': """
    Displaying Covid Message
    """,
    'version': '15.0.1.0.0',
    'category': 'Sales/Sales',
    'author': 'KAVISH SHAH',
    'website': 'http://www.aktivsoftware.com',
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'depends': [
        'base',
        'sale_management'
    ],

    'data': [
        'views/sale_order.xml',
        'views/product_product.xml',
        'views/sale_order_line.xml',
        'views/invoice_lines.xml',
        'views/sale_order_report.xml',
    ],
}