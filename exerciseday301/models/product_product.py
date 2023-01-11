

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"
    
    min_age = fields.Integer(string="Min Age")