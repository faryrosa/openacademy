# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class sessions_report_daily_wizard(models.TransientModel):
    _name = 'sessions.report.daily.wizard'
    _description = 'Sessions Daily Report'
    
    start_date = fields.Date(required=True, default=fields.Date.today())
    
    @api.multi
    def generate_report(self):
        data = {'date_start': self.start_date}

        sessions_ids = self.env['openacademy.session'].search([('start_date', '=', self.start_date)])
        sessions_brw = self.env['openacademy.session'].browse(sessions_ids)
        
        return self.env['report'].get_action(
            sessions_brw, 'openacademy.report_sessions_daily', data=data)
