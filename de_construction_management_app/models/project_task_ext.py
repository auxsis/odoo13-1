# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ProjectTaskExt(models.Model):
    _inherit = 'project.task'

    date_start = fields.Date(string='Starting Date')
    date_end = fields.Date(string='Ending Date')
