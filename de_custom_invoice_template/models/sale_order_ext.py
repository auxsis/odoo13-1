# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _


class CustomProformaInvoice1Wizard(models.TransientModel):
    _name = 'proforma.invoice1'

    def action_print_custom_proforma_invoice1(self):
        data = {
            'model': 'proforma.invoice1',
            'form': self.read()[0]
        }
        print('k..', self.read()[0])
        print('data', data)
        return self.env.ref('de_custom_invoice_template.report_action_custom_proforma1').report_action(self, data=data)

    name = fields.Char(string='Name')
    proforma_invoice_no = fields.Char(string='Proforma Invoice')
    date = fields.Date(string='Date')
    order_id = fields.Many2one(comodel_name='sale.order', string='Order No')
    fca_price_total = fields.Float(string='Total FCA Sialkot Price')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    income_term = fields.Char(string='Income Term')
    latest_shipment_date = fields.Date(string='Latest Shipment Date')
    payment_term = fields.Char(string='Payment Term')
    shipment_by = fields.Char(string='Shipment By')
    partial_shipment = fields.Char(string='Partial Shipment')
    shipment = fields.Char(string='TranShipment')


class CustomInvoice(models.Model):
    _inherit = 'sale.order'

    def custom_proforma_invoice1_button(self):
        wizard_view_id = self.env.ref(
            'de_custom_invoice_template.custom_proforma_invoice1_wizard')
        return {
            'name': _('Proforma Invoice'),
            'res_model': 'proforma.invoice1',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': wizard_view_id.id,
            'target': 'new',
        }
