# -*- coding: utf-8 -*-
# from odoo import http


# class Env/dynexcel/addons/(http.Controller):
#     @http.route('/env/dynexcel/addons//env/dynexcel/addons//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/env/dynexcel/addons//env/dynexcel/addons//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('env/dynexcel/addons/.listing', {
#             'root': '/env/dynexcel/addons//env/dynexcel/addons/',
#             'objects': http.request.env['env/dynexcel/addons/.env/dynexcel/addons/'].search([]),
#         })

#     @http.route('/env/dynexcel/addons//env/dynexcel/addons//objects/<model("env/dynexcel/addons/.env/dynexcel/addons/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('env/dynexcel/addons/.object', {
#             'object': obj
#         })
