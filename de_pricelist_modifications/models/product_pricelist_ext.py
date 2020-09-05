# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ProductPriceListItemExt(models.Model):
    _inherit = 'product.pricelist.item'

    def write(self, vals):
        parent_id = self.env.context.get('pricelist_id')
        parent_model = self.env.context.get('product.pricelist')
        # if parent_id and parent_model:
        parent_obj = self.env['product.pricelist'].browse(parent_id)
        print('parent', parent_obj)
        rec = super(ProductPriceListItemExt, self).create(vals)
        print('rec', rec)
        print('vals', vals)
        print('product', self.product_tmpl_id.name)
        price_lists = self.env['product.pricelist'].search([('id', '=', rec.pricelist_id.id)])
        print('price', price_lists)
        print('ids', price_lists.ref_price_list_ids)
        print('product', self.product_tmpl_id.name)
        for item in price_lists.ref_price_list_ids.item_ids:
            print('item', item)
            item.new({
                'pricelist_id': self.id,
                'applied_on': '1_product',
                'product_tmpl_id': self.product_tmpl_id.id,
                'base': 'list_price'
            })
        return rec


class ProductPriceListExt(models.Model):
    _inherit = 'product.pricelist'

    # @api.onchange('ref_price_list_ids')
    # def _onchange_ref_price_list_ids(self):
    #     for rec in self:
    #         for value in rec.ref_price_list_ids:
    #             print('value', value.name)

    @api.model
    def create(self, vals):
        rec = super(ProductPriceListExt, self).create(vals)
        print('vals', vals)
        if vals.get("ref_price_list_ids"):
            for value in vals.get("ref_price_list_ids"):
                print('value', value)
        return rec

    def write(self, vals):
        rec = super(ProductPriceListExt, self).write(vals)
        list = []
        print('id', self.ref_price_list_ids)
        if self.ref_price_list_ids:
            line_model = self.env['product.pricelist.item'].search([('pricelist_id', '=', self.id)])
            for line in line_model:
                print('product', line.product_tmpl_id.name)
                list.append(line.product_tmpl_id.id)
            for value in self.ref_price_list_ids:
                price_lists = self.env['product.pricelist'].search([('id', '=', value.id)])
            #     # for pl in price_lists:
            #     #     ex_items = self.env['product.pricelist.item'].search([('pricelist_id', '=', pl.id)])
            #     #     for item in /em', item.id)
            #     price_lists.item_ids.create({
            #         'product_tmpl_id': 23,
            #         'pricelist_id': self.id,
            #         'applied_on': '1_product',
            #         'base': 'list_price'
            #     })
                # for pl in price_lists:
                #     print('price', pl)
                #     price_lists.write({
                #         'item_ids': [(0, 0, {
                #             'product_tmpl_id': 23,
                #             'pricelist_id': self.id,
                #             'applied_on': '1_product',
                #             'base': 'list_price'
                #         })]
                #     })
        return rec

    ref_price_list_ids = fields.Many2many(comodel_name='product.pricelist', string='Ref PriceList',
                                          relation='product_price_rel', column1='m2m_id', column2='assets_id')
