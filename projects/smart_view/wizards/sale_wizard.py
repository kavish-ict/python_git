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

    def add_product_lines(self):
        """
        function to update sale order lines when specific products are selected in wizard
        """
        res = self.env['sale.order']
        active_id = self.env.context.get('active_id')
        record = res.browse(active_id)

        for rec in self.products_ids:
            record.write({"order_line": [(4, rec.id)]})
