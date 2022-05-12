from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Created this module."

    total_capacity = fields.Integer(string="Total Capacity")

    def calculate_total_capacity(self):
        print("----------self context", self.id)
        total = 0.0
        res = self.env['sale.order'].browse(self.id)
        for num in res.order_line:
            total += num.max_qty
        print("==========total", total)
        res['total_capacity'] = total
        print("-------------------------", res)

