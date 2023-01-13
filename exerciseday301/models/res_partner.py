from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'   
    
    date_of_birth = fields.Date(string="Date of Birth")
    @api.onchange('name')
    def onchange_name(self):
        for rec in self:
            if self.name:  
                rec.email = rec.name.replace(' ', '_').lower() + '@odoo.com'        
    
    signature = fields.Binary(string="Signature")
    