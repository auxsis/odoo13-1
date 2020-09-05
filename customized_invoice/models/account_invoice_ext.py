# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class AccountMoveLineExt(models.Model):
    _inherit = 'account.move.line'

    @api.depends('cotton', 'cotton_packing')
    def _compute_product_units(self):
        for rec in self:
            rec.cotton_units = rec.cotton * rec.cotton_packing

    @api.depends('cotton', 'cotton_packing')
    def _compute_quantity(self):
        for rec in self:
            rec.cotton_units = rec.cotton * rec.cotton_packing

    @api.depends('cotton', 'cotton_packing')
    def _compute_quantity(self):
        for rec in self:
            rec.quantity = rec.cotton * rec.cotton_packing

    @api.depends('cotton_packing', 'price_unit')
    def _compute_cotton_tp_rate(self):
        for rec in self:
            rec.cotton_tp_rate = rec.cotton_packing * rec.price_unit

    @api.depends('unit_discount', 'price_unit')
    def _compute_unit_invoice_rate(self):
        for rec in self:
            rec.unit_invoice_rate = rec.price_unit - rec.unit_discount

    @api.depends('cotton_tp_rate', 'cotton_discount')
    def _compute_cotton_invoice_rate(self):
        for rec in self:
            rec.cotton_invoice_rate = rec.cotton_tp_rate * rec.cotton_discount

    @api.depends('price_unit')
    def _compute_unit_discount(self):
        for rec in self:
            rec.unit_discount = rec.price_unit * (10.72/100)

    @api.depends('cotton_tp_rate')
    def _compute_cotton_discount(self):
        for rec in self:
            rec.cotton_discount = rec.cotton_tp_rate * (10.72/100)

    @api.depends('unit_invoice_rate', 'unit_discount')
    def _compute_discount_percentage(self):
        for rec in self:
            if rec.unit_discount:
                rec.discount_percentage = rec.unit_invoice_rate / rec.unit_discount
            else:
                rec.discount_percentage = 0.0

    @api.depends('cotton', 'cotton_tp_rate')
    def _compute_tp_value(self):
        for rec in self:
            rec.tp_value = rec.cotton * rec.cotton_tp_rate

    @api.depends('tp_value')
    def _compute_distributor_margin(self):
        for rec in self:
            rec.distributor_margin = rec.tp_value * (10.72/100)

    @api.depends('tp_value', 'distributor_margin', 'trade_amount')
    def _compute_net_amount(self):
        for rec in self:
            rec.net_amount = rec.tp_value - (rec.distributor_margin + rec.trade_amount)

    cotton = fields.Float(string='Ctn')
    cotton_packing = fields.Float(string='Ctn Packing')
    cotton_units = fields.Float(string='Units', compute='_compute_product_units', store=True)
    unit_tp_rate = fields.Float(string='T.P Rate per Unit')
    cotton_tp_rate = fields.Float(string='T.P Rate per Cotton', compute='_compute_cotton_tp_rate',
                                  store=True)
    unit_invoice_rate = fields.Float(string='Invoice Rate per Unit', compute='_compute_unit_invoice_rate',
                                     store=True)
    cotton_invoice_rate = fields.Float(string='Invoice Rate per Cotton', compute='_compute_cotton_invoice_rate',
                                       store=True)
    unit_discount = fields.Float(string='Dist Margin per Unit', compute='_compute_unit_discount',
                                 store=True)
    cotton_discount = fields.Float(string='Dist Margin per Ctn', compute='_compute_cotton_discount',
                                   store=True)
    discount_percentage = fields.Float(string='Dist Margin in %', compute='_compute_discount_percentage',
                                       store=True)
    per_unit_retail_price = fields.Float(string='Retail Price Per Unit')
    tp_value = fields.Float(string='T.P Rate in Value', compute='_compute_tp_value', store=True)
    distributor_margin = fields.Float(string='Distributor Margin', compute='_compute_distributor_margin',
                                      store=True)
    trade = fields.Float(string='Trade Offer')
    trade_amount = fields.Float(string='Trade Offer Amount')
    net_amount = fields.Float(string='Net Amount', compute='_compute_net_amount', store=True)
    per_cotton_retail_price = fields.Float(string='Retail Price per Ctn')
    price_unit = fields.Float(string='T.P Rate per Unit', digits='Product Price')
    quantity = fields.Float(string='Units', digits='Product Unit of Measure',
                            compute='_compute_quantity', store=True,
                            help="The optional quantity expressed by this line, eg: number of product sold. "
                                 "The quantity is not a legal requirement but is very useful for some reports.")
