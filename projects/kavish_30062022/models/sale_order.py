from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Created this module."

    product_id = fields.Many2one('product.product', string="Product")
    qty = fields.Integer(string="Quantity")

    @api.onchange('product_id', 'qty')
    def onchange_product_qty(self):
        new_lines = [()]
        lines = []
        print("---------------", lines)
        for rec in self:
            if self.product_id and self.qty:
                lines.append((0, 0, {
                    'product_id': rec.product_id.id,
                    'name': rec.product_id.name,
                    'price_unit': rec.product_id.list_price,
                    'product_uom_qty': rec.qty,
                    'product_uom': rec.product_id.uom_id.id,
                }))
            self.update({
                'order_line': lines
            })

    # @api.onchange('qty')
    # def onchange(self):
    #     for line in self.order_line:
    #         line.write({'product_uom_qty': self.qty})

    # if self.product_id.id == self.product_id.id:
    #     new_lines.append((0, 0, {
    #         'product_id': rec.product_id.id,
    #         'name': rec.product_id.name,
    #         'product_uom_qty': rec.qty,
    #         'product_uom': rec.product_id.uom_id.id,
    #     }))
    # self.update({
    #         'order_line': new_lines
    #     })

    # if self.product_id.id == self.product_id.id:
    # print("=======================new lines", new_lines)

    # @api.onchange('product_id', 'qty')
    # def onchange_product_id(self):
    #     lines = []
    #     print("=====================================")
    #     for rec in self:
    #         if self.product_id and self.qty:
    #             if self.product_id.id == self.product_id.id:
    #                 lines.append((0, 0, {
    #                     'product_id': rec.product_id.id,
    #                     'name': rec.product_id.name,
    #                     'product_uom_qty': rec.qty,
    #                     'product_uom': rec.product_id.uom_id.id,
    #                 }))
    #     self.update({
    #             'order_line': lines
    #         })
    #     print("------------lines----------------", lines)
