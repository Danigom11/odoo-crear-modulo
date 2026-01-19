{
    'name': 'Economía Circular Velas',
    'version': '1.0',
    'summary': 'Gestión de reciclaje y retorno de envases de velas',
    'author': '2º DAM - SGE- Odoo',
    'category': 'Sustainability',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/economia_view.xml',
        'views/tipo_residuo_view.xml',
        'report/certificado_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}