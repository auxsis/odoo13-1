# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ProjectProjectExt(models.Model):
    _inherit = 'project.project'

    analytic_account_id = fields.Many2one(comodel_name='account.journal', string='Analytic Account')
    sub_task_project_id = fields.Many2one(comodel_name='project.project', string='Sub-task Project')
    time_sheets = fields.Boolean(string='TimeSheets')
    customer_type = fields.Selection([('agricultural', 'Agricultural'),
                                      ('residential', 'Residential'),
                                      ('commercial', 'Commercial'),
                                      ('institutional', 'Institutional'),
                                      ('industrial', 'Industrial'),
                                      ('heavy_civil', 'Heavy Civil'),
                                      ('environmental', 'Environmental'),
                                      ('other', 'Other')],
                                     string='Type of Construction')
    location_id = fields.Many2one(comodel_name='res.partner', string='Location')
