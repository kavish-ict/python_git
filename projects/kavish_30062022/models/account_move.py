from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = "Created this module."

    # length = fields.Float(string="Length", related="product_id.length")
    # total_length = fields.Float(string="Total Length", compute="create_invoices")

    # @api.model
    # def create(self, vals):
    #     res = super(AccountMove, self).create(vals)
    #     new_env = self.env['sale.order'].browse(self.env.context.get('active_id'))
    #     print("____________________________---_-__", new_env.order_line.total_length)
    #     print("------------------------------------------------", new_env)
    #     new_lines = []
    #     for rec in self:
    #         new_lines.append((0, 0, {
    #             'total_length': new_env.order_line.total_length,
    #             'price_subtotal': new_env.order_line.price_subtotal
    #         }))
    #     self.update({
    #        'invoice'
    #     })
    #     # for rec in self.invoice_line_ids:
    #     #     print("+++++++++++++++++++")
    #     #     rec.total_length = new_env.order_line.total_length
    #     #     rec.price_subtotal = new_env.price_subtotal
    #     return res
