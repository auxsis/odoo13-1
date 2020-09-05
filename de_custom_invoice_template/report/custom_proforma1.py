# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class CustomProforma(models.AbstractModel):
    _name = 'report.de_custom_invoice_template.report_custom_proforma_view'

    @api.model
    def _get_report_values(self, docids, data):
        domain = []
        if data['form']['order_id']:
            domain.append(('id', '=', data['form']['order_id']))
        print(domain)
        if data['form']['order_id']:
            order = data['form']['order_id']
        if domain:
            docs = self.env['sale.order'].search(domain)
        # else:
        #     docs = self.env['sale.order'].search([])
        print('date', docs)
        return {
            'doc_ids': self.ids,
            'data': data,
            'docs': docs,
        }
