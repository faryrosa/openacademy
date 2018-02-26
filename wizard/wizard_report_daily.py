# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SessionsDailyReport(models.TransientModel):
    _name = 'sessions.daily.report.wizard'
    _description = 'Sessions Daily Report'
    
    start_date = fields.Date(required=True, default=fields.Date.today())
    
    @api.multi
    def generate_report(self):
        data = {'date_start': self.start_date}

        sessions = self.env['openacademy.session'].search([('start_date', '=', self.start_date)])
        sessions_ids = sessions.mapped('id')
        
        return self.env['report'].get_action(
            sessions_ids, 'openacademy.report_sessions_daily', data=data)
