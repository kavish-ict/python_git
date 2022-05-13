from odoo import models, fields, api


class BulkProducts(models.Model):
    _name = 'bulk.products'
    _description = "Created this module."

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    master_product_id = fields.Many2one("product.template",
                                        string="Master Product")
    user_id = fields.Many2one("res.partner", string="User")
    bulk_products_ids = fields.One2many("bulk.products.line",
                                        "bulk_id", string="Bulk Products")


class BulkProductLine(models.Model):
    _name = 'bulk.products.line'
    _description = 'bulk products line model'

    product_id = fields.Many2one('product.product', string="Product",
                                 domain=[('detailed_type', '=', 'product')])
    description = fields.Char(string="Description")
    quantity = fields.Integer(string="Quantity", default="1")
    bulk_id = fields.Many2one('bulk.products')

