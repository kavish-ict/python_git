from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _description = "Created this module."

    length = fields.Float(string="Length")
