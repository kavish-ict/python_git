from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Created this module."

    bulk_product_template = fields.Many2one('bulk.products', string="Bulk Product Template")

    @api.onchange('bulk_product_template')
    def on_change_bulk(self):
        new_lines = []
        new_env = self.env['bulk.products'].browse(self.bulk_product_template.id)
        for res in new_env.bulk_products_ids:
            new_lines.append((0, 0, {
                'product_id': res.product_id.id,
                'name': res.description,
                'product_uom_qty': res.quantity,
                'product_uom': res.product_id.uom_id.id,
            }))
        self.update({'order_line': new_lines})
        print("=======================new lines", new_lines)
        print("-----------------------", self._context)
