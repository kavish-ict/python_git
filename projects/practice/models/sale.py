# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_reference = fields.Char(string="Customer Reference",related="partner_id.customer_reference")
