from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = "Created this module."

    length = fields.Float(string="Length", related="product_id.length")
    total_length = fields.Float(string="Total Length", compute="_compute_amount")

    @api.depends('length')
    def _compute_amount(self):
        # self.total_length =
        # print("_____________________res______________", res)
        res = super(SaleOrderLine, self)._compute_amount
        for rec in self:
            rec.total_length = rec.length * rec.product_uom_qty
            rec.price_subtotal = rec.length * rec.product_uom_qty * rec.price_unit
        return res
