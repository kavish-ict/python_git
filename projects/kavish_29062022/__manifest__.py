{
    'name': 'Frontend Task',
    'summary': """Displaying Covid Message""",
    'description': """
    Displaying Covid Message
    """,
    'version': '15.0.1.0.0',
    'category': 'Website/Website',
    'author': 'KAVISH SHAH',
    'website': 'http://www.aktivsoftware.com',
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'depends': [
        'base',
        'website',
        'website_sale'
    ],

    'data': [
        'security/message_security.xml',
        'views/res_config_settings.xml',
        'views/frontend.xml',
    ],
}