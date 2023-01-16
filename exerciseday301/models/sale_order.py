

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    total_item = fields.Integer(string="Total Items", compute='_compute_count_total')
    @api.depends('order_line.product_uom_qty')
    def _compute_count_total(self):
        for rec in self:
            rec.total_item = sum(rec.order_line.mapped('product_uom_qty'))
    #By Loop
    # def _compute_count_total(self):
    #     for rec in self:
    #         count_item = 0                
    #         for order_line in rec.order_line:
    #           count_item = count_item + order_line.product_uom_qty  
    #         rec.total_item = count_item

    phone = fields.Char(string="Phone", related="partner_id.phone")
    mobile = fields.Char(string="Mobile", related="partner_id.mobile")

    #Wizard
    def action_set_quantity(self):
        return {
            'name': _('Set Sales Order Quantity'),
            'view_mode': 'form',
            'res_model': 'sale.order.quantity',
            'view_id': self.env.ref('exerciseday301.set_order_quantity_wizard').id,
            'type': 'ir.actions.act_window',
            'context': {'default_sale_order': self.id},
            'target': 'new'
        }
