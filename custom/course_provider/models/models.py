# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Instructor(models.Model):
    _name = 'openacademy.instructor'
    _description = 'Open Academy instructor'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    image = fields.Binary(string="Image")
