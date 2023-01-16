

from odoo import models, fields, api


class SaleOrderQuantity(models.TransientModel):
    _name = 'sale.order.quantity'
    _description = 'Set quantity by batch'

    quantity = fields.Integer('Quantity', required=True)
    sale_order = fields.Many2one('sale.order', string='Sale Order', required=True)
    
    def action_set_quantity(self):
        for rec in self:
            for order_line in rec.sale_order.order_line:
                order_line.product_uom_qty = rec.quantity
        return
    

