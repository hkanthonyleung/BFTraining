from odoo import api, fields, models

class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char()
    isbn = fields.Char("ISBN")
    summary = fields.Text()
    author = fields.Char()
    copies = fields.Integer()
