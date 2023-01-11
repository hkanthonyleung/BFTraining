# -*- coding: utf-8 -*-
# from odoo import http


# class Exerciseday301(http.Controller):
#     @http.route('/exerciseday301/exerciseday301', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exerciseday301/exerciseday301/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('exerciseday301.listing', {
#             'root': '/exerciseday301/exerciseday301',
#             'objects': http.request.env['exerciseday301.exerciseday301'].search([]),
#         })

#     @http.route('/exerciseday301/exerciseday301/objects/<model("exerciseday301.exerciseday301"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exerciseday301.object', {
#             'object': obj
#         })
