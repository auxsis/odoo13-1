# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.safe_eval import safe_eval
from odoo.tools.misc import format_date


class ConStages(models.Model):
    _name = 'con.stages'
    _description = 'Project Stages'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)


