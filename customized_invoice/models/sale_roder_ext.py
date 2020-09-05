# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class SaleOrderLineExt(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('cotton', 'cotton_packing')
    def _compute_product_units(self):
        for rec in self:
            rec.cotton_units = rec.cotton * rec.cotton_packing

    @api.depends('cotton', 'cotton_packing')
    def _compute_product_uom_qty(self):
        for rec in self:
            rec.product_uom_qty = rec.cotton * rec.cotton_packing

    @api.depends('cotton_packing', 'price_unit')
    def _compute_cotton_tp_rate(self):
        for rec in self:
            rec.cotton_tp_rate = rec.cotton_packing * rec.price_unit

    @api.depends('unit_discount', 'price_unit')
    def _compute_unit_invoice_rate(self):
        for rec in self:
            rec.unit_invoice_rate = rec.price_unit * rec.unit_discount

    @api.depends('cotton_tp_rate', 'cotton_discount')
    def _compute_cotton_invoice_rate(self):
        for rec in self:
            rec.cotton_invoice_rate = rec.cotton_tp_rate * rec.cotton_discount

    @api.depends('price_unit')
    def _compute_unit_discount(self):
        for rec in self:
            rec.unit_discount = rec.price_unit * (10.72 / 100)

    @api.depends('cotton_tp_rate')
    def _compute_cotton_discount(self):
        for rec in self:
            rec.cotton_discount = rec.cotton_tp_rate * (10.72 / 100)

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
            rec.distributor_margin = rec.tp_value * (10.72 / 100)

    @api.depends('tp_value', 'distributor_margin', 'trade_amount')
    def _compute_net_amount(self):
        for rec in self:
            rec.net_amount = rec.tp_value - (rec.distributor_margin + rec.trade_amount)

    # passing value from sale order line to account move line
    def _prepare_invoice_line(self):
        res = super(SaleOrderLineExt, self)._prepare_invoice_line()
        res.update({'cotton': self.cotton,
                    'cotton_packing': self.cotton_packing,
                    'quantity': self.product_uom_qty,
                    'price_unit': self.price_unit,
                    'per_unit_retail_price': self.per_unit_retail_price,
                    'trade': self.trade,
                    'trade_amount': self.trade_amount,
                    'per_cotton_retail_price': self.per_cotton_retail_price})
        return res

    # @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    # def _compute_amount(self):
    #     """
    #     Compute the amounts of the SO line.
    #     """
    #     for line in self:
    #         price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
    #         taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
    #                                         product=line.product_id, partner=line.order_id.partner_shipping_id)
    #         print('1', taxes['total_excluded'])
    #         print('1', line.trade_amount)
    #         line.update({
    #             'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
    #             'price_total': taxes['total_included'],
    #             'price_subtotal': taxes['total_excluded'] - line.trade_amount,
    #         })
    #         if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
    #                 'account.group_account_manager'):
    #             line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])

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
    product_uom_qty = fields.Float(string='Units', digits='Product Unit of Measure', required=True, default=1.0,
                                   compute='_compute_product_uom_qty', store=True)
    price_unit = fields.Float(string='T.P Rate per Unit', required=True, digits='Product Price', default=0.0)
