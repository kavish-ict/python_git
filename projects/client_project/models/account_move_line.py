from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = "Created this module."

    delivery_address_id = fields.Many2one('res.partner', string="Delivery Address", domain=[("type", "=", "delivery")])
    vendor_id = fields.Many2one("res.partner", string="Vendor", domain=[("supplier_rank", ">", 4)])
    vendor_price = fields.Float(string="Vendor price")
    planned_gp = fields.Float(string="Planned GP %")
    description = fields.Text(string="Description", compute="add_description")

    @api.onchange('price_unit', 'vendor_price')
    def _compute_price(self):
        for rec in self:
            if rec.price_unit or rec.vendor_price:
                rec.planned_gp = ((rec.price_unit - rec.vendor_price) / rec.price_unit) * 100

    # @api.depends('delivery_address_id', 'name')
    # def _compute_description_id(self):
    #     for rec in self:
    #         if rec.delivery_address_id and rec.name:
    #             rec.description = rec.name + rec.delivery_address_id.name

    @api.depends('delivery_address_id', 'name')
    def add_description(self):
        for rec in self:
            if rec.delivery_address_id and rec.name:
                rec.description = rec.name + rec.delivery_address_id.name
            else:
                rec.description = "add description"
