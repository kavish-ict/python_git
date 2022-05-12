from odoo import models, fields, api


class PracticalPaper(models.Model):
    _inherit = 'product.product'
    _description = "Created this module."

    qty_on_order = fields.Float(string="qty on order", default=1.0)

    def test(self):
        print("=================",self.env.context.get('active_id'))
