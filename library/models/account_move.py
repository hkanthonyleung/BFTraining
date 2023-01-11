from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    new_field = fields.Char("New")
