# -*- coding: utf-8 -*-

from flectra import models, fields, api, tools
from datetime import datetime
from dateutil import relativedelta

class CWIPAsset(models.AbstractModel):
    _name = "report.assets_cwip_report.report_cwip_asset_view"

    @api.model
    def get_report_values(self, docids, data):
        #making the domain to filter the recordset of cwip.assets.line
        domain = []
        if data['form']['cwip_assets']:
            domain.append(('cwip_asset_id.id', 'in' ,data['form']['cwip_assets']))
        if data['form']['date_from']:
            domain.append(('date', '>=' ,data['form']['date_from']))
        if data['form']['date_to']:
            domain.append(('date', '<=', data['form']['date_to']))
        if data['form']['product_ids']:
            domain.append(('product_id.id', 'in', data['form']['product_ids']))
        if data['form']['vendor_id']:
            domain.append(('partner_id.id', '=', data['form']['vendor_id'][0]))




        print(domain)
        if data['form']['cwip_assets']:
            docs = self.env['cwip.assets'].search([('id', 'in' ,data['form']['cwip_assets'])])
        else:
            docs = self.env['cwip.assets'].search([])


        docs_line = self.env['account.invoice.line'].search(domain)
        return {
            'doc_ids': self.ids,
            'data': data,
            'docs':docs,
            'docs_line':docs_line,

            }




