# -*- coding: utf-8 -*-
# from odoo import http


# class DeReferencePricelist(http.Controller):
#     @http.route('/de_reference_pricelist/de_reference_pricelist/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_reference_pricelist/de_reference_pricelist/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_reference_pricelist.listing', {
#             'root': '/de_reference_pricelist/de_reference_pricelist',
#             'objects': http.request.env['de_reference_pricelist.de_reference_pricelist'].search([]),
#         })

#     @http.route('/de_reference_pricelist/de_reference_pricelist/objects/<model("de_reference_pricelist.de_reference_pricelist"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_reference_pricelist.object', {
#             'object': obj
#         })
