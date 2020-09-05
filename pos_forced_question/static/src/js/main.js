/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */
odoo.define('pos_forced_question.pos_forced_question', function(require) {
	"use strict";
	var models = require('point_of_sale.models');
	var core = require('web.core');
	var gui = require('point_of_sale.gui');
	var core = require('web.core');
	var _t = core._t;
	var screens = require('point_of_sale.screens');
	var popup_widget = require('point_of_sale.popups');
	var SuperOrder = models.Order;
	var SuperOrderline = models.Orderline;
	var SuperOrderWidget = screens.OrderWidget;
	var QWeb = core.qweb;

	exports.PosModel = Backbone.Model.extend({
	    initialize: function(session, attributes) {
        Backbone.Model.prototype.initialize.call(this, attributes);
        var  self = this;
        this.flush_mutex = new Mutex();                   // used to make sure the orders are sent to the server once at time
        this.chrome = attributes.chrome;
        this.gui    = attributes.gui;

        this.proxy = new devices.ProxyDevice(this);              // used to communicate to the hardware devices via a local proxy
        this.barcode_reader = new devices.BarcodeReader({'pos': this, proxy:this.proxy});

        this.proxy_queue = new devices.JobQueue();           // used to prevent parallels communications to the proxy
        this.db = new PosDB();                       // a local database used to search trough products and categories & store pending orders
        this.debug = core.debug; //debug mode

        // Business data; loaded from the server at launch
        this.company_logo = null;
        this.company_logo_base64 = '';
        this.currency = null;
        this.shop = null;
        this.company = null;
        this.user = null;
        this.users = [];
        this.partners = [];
        this.cashregisters = [];
        this.taxes = [];
        this.pos_session = null;
        this.config = null;
        this.units = [];
        this.units_by_id = {};
        this.default_pricelist = null;
        this.order_sequence = 1;
        this.is_partner_pos = null;
        window.posmodel = this;

        // these dynamic attributes can be watched for change by other models or widgets
        this.set({
            'synch':            { state:'connected', pending:0 },
            'orders':           new OrderCollection(),
            'selectedOrder':    null,
            'selectedClient':   null,
            'cashier':          null,
        });

        this.get('orders').bind('remove', function(order,_unused_,options){
            self.on_removed_order(order,options.index,options.reason);
        });

        // Forward the 'client' attribute on the selected order to 'selectedClient'
        function update_client() {
            var order = self.get_order();
            this.set('selectedClient', order ? order.get_client() : null );
        }
        this.get('orders').bind('add remove change', update_client, this);
        this.bind('change:selectedOrder', update_client, this);

        // We fetch the backend data on the server asynchronously. this is done only when the pos user interface is launched,
        // Any change on this data made on the server is thus not reflected on the point of sale until it is relaunched.
        // when all the data has loaded, we compute some stuff, and declare the Pos ready to be used.
        this.ready = this.load_server_data().then(function(){
            return self.after_load_server_data();
        });
    },

	})

});
