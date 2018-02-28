# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SessionsDailyINDReport(models.TransientModel):
    _name = 'sessions.daily.report.wizard.independ'
    _description = 'Sessions Daily IND Report'
    
    start_date = fields.Date(required=True, default=fields.Date.today())
    sessions_ids = fields.Many2many('openacademy.session', string="Sessions")
    
    @api.multi
    def generate_report(self):
        
        sessions = self.env['openacademy.session'].search([('start_date', '=', self.start_date)])
        self.sessions_ids = sessions.mapped('id')
        
        return self.env['report'].get_action(
            self, 'openacademy.report_sessions_daily_ind_view')
