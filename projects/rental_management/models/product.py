"""
new module
"""
from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "inherit product template object"

    is_rental = fields.Boolean(string="Is Rental")
    rental_type_id = fields.Many2one('rental.type',
                                     string="Rental Type",
                                     invisible=True)
