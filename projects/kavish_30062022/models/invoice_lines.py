from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = "Created this module."

    length = fields.Float(string="Length", related="product_id.length")
    total_length = fields.Float(string="Total Length", compute="_compute_amount")

    @api.depends('length')
    def _compute_amount(self):
        for rec in self:
            rec.total_length = rec.length * rec.quantity
            rec.price_subtotal = rec.length * rec.quantity * rec.price_unit
