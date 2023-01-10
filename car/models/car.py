from odoo import models, fields, api


class car(models.Model):
    _name = 'car.car'
    _description = 'car.car'

    name = fields.Char(string="Name", required=True)
    production_date = fields.Date(string="Production Date")
    brand = fields.Selection(
        string="Brand",
        selection=[
            ("benz", "Mercedes Benz"), 
            ("honda", "Honda")], default="honda")
    mileage = fields.Integer(string="Mileage")
    picture = fields.Binary(string="Picture")
    price = fields.Float(string="Price")
    rented = fields.Boolean(string="Rented")