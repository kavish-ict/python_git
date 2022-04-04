# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Many2one


class SaleWizard(models.Model):
    """
    created wizard
    """
    _name = "task.wizard"
    _description = 'wizard created for sale order'

    products_ids = fields.Many2many("product.product", string='Products')

    def add_order_line(self):
        if self.products_ids:
            rec = self.env[self._context.get('active_model', [])].browse(self._context.get('active_ids', []))
            for product in self.products_ids:
                rec.write({'order_line': [(0, 0, {'product_id': product.id})]})

