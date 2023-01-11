from odoo import api, fields, models

class LibraryRental(models.Model):
    _name = "library.rental"

    renter = fields.Char("Renter")
    book = fields.Many2one("library.book")
    date_rent = fields.Date("Rental Date")
    date_end = fields.Date("Max Return Date")
