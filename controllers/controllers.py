# -*- coding: utf-8 -*-
# from odoo import http


# class CustomgyhModule(http.Controller):
#     @http.route('/customgyh_module/customgyh_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customgyh_module/customgyh_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customgyh_module.listing', {
#             'root': '/customgyh_module/customgyh_module',
#             'objects': http.request.env['customgyh_module.customgyh_module'].search([]),
#         })

#     @http.route('/customgyh_module/customgyh_module/objects/<model("customgyh_module.customgyh_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customgyh_module.object', {
#             'object': obj
#         })
