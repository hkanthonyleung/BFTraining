from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'   

    book_rental = fields.One2many("library.rental", "renter2", string="Book Rental")