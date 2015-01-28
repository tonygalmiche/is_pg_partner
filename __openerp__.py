# -*- coding: utf-8 -*-

{
    'name': 'Client / Fournisseur Plastigray',
    'version': '1.0',
    'category': 'InfoSaône',
    'description': """
Client / Fournisseur Plastigray
""",
    'author': 'Tony GALMICHE / Asma BOUSSELMI',
    'maintainer': 'InfoSaone',
    'website': 'http://www.infosaone.com',
    'depends': ['base', 'document', 'is_partner', 'is_plastigray'],
    'data': ['security/is_pg_partner_security.xml',
             'security/ir.model.access.csv',
             'is_pg_partner_view.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
