from odoo import models, fields, api


class BatchOrderWizard(models.TransientModel):
    _name = 'batch.order.wizard'

    batch_order_lines_ids = fields.One2many('batch.order.line', 'batch_id', string="Sale order lines")

    def test(self):
        pass

    @api.model
    def default_get(self, fields):
        res = super(BatchOrderWizard, self).default_get(fields)
        record_active_id = self.env['batch.sale.workflow'].browse(self.env.context.get('active_id'))
        new_batch_lines = []
        for rec in record_active_id.order_ids.order_line:
            new_batch_lines.append((0, 0, {
                'product_id': rec.product_id.id,
                'description': rec.name,
                'quantity': rec.product_uom_qty,
                'price': rec.price_unit
            }))
        print("_________new lines______-------------------------", new_batch_lines)
        res.update({'batch_order_lines_ids': new_batch_lines})
        return res

    def submit_record(self):
        record_active_id = self.env['batch.sale.workflow'].browse(self.env.context.get('active_id'))
        print("--------batch active id------------", record_active_id)
        # wizard_active_id = self.browse(self.env.context.get('active_id'))
        # print("--------wizard active id------------", wizard_active_id)
        new_order_lines = []
        for record in self.batch_order_lines_ids:
            print("------record----------", record, "\n", record.product_id.id, "\n", record.description, "\n", record.quantity, "\n", record.price, "\n", record.product_id.uom_id.id)
            new_order_lines.append((0, 0, {
                'product_id': record.product_id.id,
                'name': record.description,
                'product_uom_qty': record.quantity,
                'price_unit': record.price,
                'product_uom': record.product_id.uom_id.id,
            }))
        res = self.env['sale.order'].create({
                'partner_id': record_active_id.partner_id.id,
                'order_line': new_order_lines
            })


class BatchOrderLine(models.TransientModel):
    _name = 'batch.order.line'

    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Char(string="Description")
    quantity = fields.Integer(string="Quantity")
    price = fields.Float(string="Price")
    batch_id = fields.Many2one('batch.order.wizard')
