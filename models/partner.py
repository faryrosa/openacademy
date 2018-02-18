# -*- coding: utf-8 -*-

from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'
    
    #Addd new column to the res.partner model, by default partners are not
    #instructors
    instructor = fields.Boolean("Instructor", default=False)
    
    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
