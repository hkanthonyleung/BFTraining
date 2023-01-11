

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"    
    min_age = fields.Integer(string="Min Age", related="product_id.min_age")