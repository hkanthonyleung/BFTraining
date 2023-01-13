from odoo import api, fields, models

class LibraryRental(models.Model):
    _name = "library.rental"

    renter = fields.Char("Renter")
    book = fields.Many2one("library.book")
    date_rent = fields.Date("Rental Date")
    date_end = fields.Date("Max Return Date")
    overdue_fine = fields.Float("Overdue Fine",  compute='_compute_overdue_fine')

    @api.depends('date_end')
    def _compute_overdue_fine(self):
        today = fields.Date.today()            
        for rec in self:
            rec.overdue_fine = 0
            if rec.date_end:
                temp = (today - rec.date_end).days
                if temp > 0:
                    rec.overdue_fine = temp * 2
    

    # @api.depends('date_end')
    # def _compute_overdue_fee(self):
    #     today = fields.Date.today()
    #     for rec in self:
    #         rec['overdue_fee'] = 0
    #         if rec.date_end and today > rec.date_end:
    #             days_overdue = (today - rec.date_end).days
    #             rec['overdue_fee'] = days_overdue * 2