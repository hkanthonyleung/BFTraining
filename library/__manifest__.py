# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Library',
    'description': """
        Library
    """,
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/library_book.xml",
        "views/library_rental.xml",
        "views/menus.xml",
        "reports/action.xml",
        "reports/res_partner.xml",
        "security/library.xml",
        "security/ir_rule.xml"
    ],
    'license': 'LGPL-3',
}
