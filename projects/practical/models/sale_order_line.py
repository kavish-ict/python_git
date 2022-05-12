from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = "Created this module."

    max_qty = fields.Float(string="Max. Qty Allowed", related="product_id.qty_on_order")
    total_capacity = fields.Integer(string="Total Capacity")
