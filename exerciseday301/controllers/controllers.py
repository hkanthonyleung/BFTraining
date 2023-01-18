#-*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request
from dateutil.relativedelta import relativedelta
from datetime import datetime

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
