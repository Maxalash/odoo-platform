# -*- coding: utf-8 -*-
# from odoo import http


# class CourseProvider(http.Controller):
#     @http.route('/course_provider/course_provider/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course_provider/course_provider/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('course_provider.listing', {
#             'root': '/course_provider/course_provider',
#             'objects': http.request.env['course_provider.course_provider'].search([]),
#         })

#     @http.route('/course_provider/course_provider/objects/<model("course_provider.course_provider"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course_provider.object', {
#             'object': obj
#         })
