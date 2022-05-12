from odoo import models, fields, api


class BulkProducts(models.Model):
    _name = 'bulk.products'
    _description = "Created this module."

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    master_product_id = fields.Many2one("product.template", string="Master Product")
    user_id = fields.Many2one("res.partner", string="User")
    bulk_products = fields.One2many("product.product", "name")

