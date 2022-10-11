# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'
    _inherit= 'openacademy.instructor'

    name = fields.Char(string ='title', required=True)
    description = fields.Text()
    state = fields.Selection([
      ('on_going', 'On going'),
      ('stopped', 'Stopped')
    ], required=True, default='stopped')
    instructor_id = fields.Many2one('openacademy.instructor', 
        string="Instructor")





