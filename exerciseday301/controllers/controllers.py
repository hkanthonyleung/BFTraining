#-*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request
from dateutil.relativedelta import relativedelta
from datetime import datetime
import json

class Exerciseday301(http.Controller):
    @http.route('/testing', auth='public', type='http')
    def testing(self, **kw):
        return "Hello, world"

    @http.route('/testing2/<string:date>', auth='public', type='http')
    def testing2(self, date, **kw):
        total_sales = sum(request.env['sale.order'].search([('date_order','<=', datetime.strptime(date, '%Y-%m-%d'))]).mapped('amount_total'))
        return "%s" % total_sales
    
    @http.route('/testing3', auth='public', type='http')
    def testing3(self, **kw):
        total_sales = sum(request.env['sale.order'].search([('date_order','<=', fields.Date.today() - relativedelta(days=2))]).mapped('amount_total'))
        return "%s" % total_sales

    @http.route('/ex8', auth='public', type='http')
    def ex8(self, **kw):
        return request.render('exerciseday301.total_amount')

    @http.route("/sale_total")
    def sale_total(self, date=None, **kw):
        if request.httprequest.method == 'POST':
            return request.redirect('/total/' + date)
        sales = request.env['sale.order'].search([])
        return "%s" % sum(sales.mapped('amount_total'))

    @http.route('/total/<string:date>', auth='public', type='http')
    def total(self, date, **kw):
        date_time = datetime.strptime(date, '%Y-%m-%d') 
        total_sales = sum(request.env['sale.order'].search([('date_order','<=', date_time)]).mapped('amount_total'))
        return "%s" % total_sales

    @http.route('/testing4', auth='public', type='http')
    def testing4(self, **kw):
        value = {
        "language": 'language',
        "company": 'company',
        "Itemid": 'Itemid',
        "price": 3
        }
        return json.dumps(value)

    @http.route('/fine', auth='public', type='http')
    def fine(self, **kw):
        records = request.env['library.rental'].search([('overdue_fine', '>', 0)])
        value = {}
        for record in records:
            entry = {'name' : record.renter2.display_name}
            value.update(entry)
        json.dumps(value)

    
    @http.route("/fines")
    def fines(self, **kw):
        rental_groups = request.env['library.rental'].read_group([], ['overdue_fine:sum'], ['renter'])
        user_fee = {}
        for group in rental_groups:
            user_fee[group['renter'][0]] = group['overdue_fine']
        return json.dumps(user_fee)
    

    @http.route("/maxoverdue")
    def maxoverdue(self, **kw):
        max_val = max(request.env['library.rental'].search([('overdue_fine', '>', 0)]).mapped('overdue_fine'))
        return "%s" % max_val
    
    @http.route("/overdue")
    def overdue(self, **kw):
        highest_rent = request.env['library.rental'].search([], order="overdue_fine desc", limit=1)
        return "%s" % highest_rent.overdue_fine
  


    @http.route('/web/session/auth', type='json', auth='none')
    def authenticate(self, db, login, password, base_location=None):
        request.session.authenticate(db, login, password)
        return request.env['ir.http'].session_info()
    


    # @http.route('/exerciseday301/exerciseday301/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('exerciseday301.listing', {
    #         'root': '/exerciseday301/exerciseday301',
    #         'objects': http.request.env['exerciseday301.exerciseday301'].search([]),
    #     })

    # @http.route('/exerciseday301/exerciseday301/objects/<model("exerciseday301.exerciseday301"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('exerciseday301.object', {
    #         'object': obj
    #     })
