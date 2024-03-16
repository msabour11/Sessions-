# -*- coding: utf-8 -*-
# from odoo import http


# class Accademy(http.Controller):
#     @http.route('/accademy/accademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/accademy/accademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('accademy.listing', {
#             'root': '/accademy/accademy',
#             'objects': http.request.env['accademy.accademy'].search([]),
#         })

#     @http.route('/accademy/accademy/objects/<model("accademy.accademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('accademy.object', {
#             'object': obj
#         })

