"""
new module
"""
from odoo import models, fields


class ExamWizard(models.TransientModel):
    """
    class created for exam wizard
    """
    _name = 'exam.wizard'
    _description = "create new object for exam"

    product_ids = fields.One2many("saleorder.wizard", "quantity" , string="Product")

    def create_so(self):
        """
        created function to set sale order  from wizard
        """
        self.env[self._context.get('active_model', [])].browse(self._context.get('active_ids', []))
        print("-------------------")
        # res = self.env["sale.order"]
        # new = self.env["sale.order.line"]
        # for rec in self.product_ids:
        #     res.write({'order_line': (0, 0, {'quantity': rec.id})})

        # order_lines = []
        # for product in res:
        #     if product.partner_id == 22:
        # order_lines.append((0, 0, {
        #     'product_id': 26
        # }))
        # res.update({'order_line': self.product_ids})
    #
    # def create_wizard_record(self):
    #     # res = self.env["res.partner"]
    #     new_id = self.env['res.partner'].create({
    #         'name': "xander",
    #         # 'order_line': self.product_ids,
    #     })
    #     new = self.env["exam.wizard"]
    #     res = self.env["sale.order"].write({
    #         "order_line": new.product_ids
    #     })


class NewField(models.TransientModel):
    """
    class created for sale order wizard
    """
    _name = "saleorder.wizard"
    _description = "wizard for sale order"

    new_product_id = fields.Many2one("product.product", string="product")
    quantity = fields.Integer(string="Quantity")
    unit_price = fields.Float(string="Unit Price", related="new_product_id.list_price")
