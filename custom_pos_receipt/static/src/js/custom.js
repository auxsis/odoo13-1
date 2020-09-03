odoo.define('custom_pos_receipt.pos_order_extend', function (require) {
"use strict";
   var models = require('point_of_sale.models');
   var screens = require('point_of_sale.screens');
   var core = require('web.core');
   var QWeb = core.qweb;
//   {
//        model:  'res.partner',
//        fields: [ 'name'],
//   },
   models.load_fields('pos.order',['invoice_number']);
//   models.load_fields('res.company',['currency_id', 'email', 'street2', 'website', 'company_registry', 'vat', 'name', 'phone', 'partner_id' , 'country_id', 'tax_calculation_rounding_method', 'social_facebook', 'social_instagram']);

});