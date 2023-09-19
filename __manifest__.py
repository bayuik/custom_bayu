{
    'name': "Custom Bayuik",
    'version': '1.0',
    'summary': """Integration between sale and purchase""",
    'description': """Integration between sale and purchase""",
    'category': 'sale',
    'author': 'Bayuik',
    'company': 'Bayuik',
    'maintainer': 'Bayuik',
    'website': "https://www.bayuik.my.id",
    'depends': ['base', 'sale', 'sale_management', 'purchase'],
    'data': [
        'views/sale_order_views.xml',
        'wizard/import_so_lines.xml',
        'security/ir.model.access.csv'
    ],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}
