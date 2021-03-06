# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from . import config
from . import update

from collections import defaultdict
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression


class StockRule(models.Model):
    _inherit = 'stock.rule'

    #     list1 = []
    #     list1.append(origin)

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values,
                         bom):
        date_deadline = fields.Datetime.to_string(self._get_date_planned(product_id, company_id, values))
        config.list12.append(origin)

        return {
            'origin': origin,
            'sale_id': config.list12[0],
            'product_id': product_id.id,
            'product_qty': product_qty,
            'product_uom_id': product_uom.id,
            'location_src_id': self.location_src_id.id or self.picking_type_id.default_location_src_id.id or location_id.id,
            'location_dest_id': location_id.id,
            'bom_id': bom.id,
            'date_deadline': date_deadline,
            'date_planned_finished': fields.Datetime.from_string(values['date_planned']),
            'date_planned_start': date_deadline,
            'procurement_group_id': False,
            'propagate_cancel': self.propagate_cancel,
            'propagate_date': self.propagate_date,
            'propagate_date_minimum_delta': self.propagate_date_minimum_delta,
            'orderpoint_id': values.get('orderpoint_id', False) and values.get('orderpoint_id').id,
            'picking_type_id': self.picking_type_id.id or values['warehouse_id'].manu_type_id.id,
            'company_id': company_id.id,
            'move_dest_ids': values.get('move_dest_ids') and [(4, x.id) for x in values['move_dest_ids']] or False,
            'user_id': False,
        }


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_id = fields.Char(string='Ref Sale')

    # @api.depends('origin')
    # def _compute_sale_ref(self):
    #     for list in self:
    #         test = self.env['sale.order'].search([('name','=', list.origin)], limit=1)
    #         list.sale_id = test.name


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        #         vals = {
        #             'sale_id': self.name,
        #         }
        #         test = self.env['mrp.production'].write(vals)
        res = super(SaleOrder, self).action_confirm()
        config.list12 = []
        return res
