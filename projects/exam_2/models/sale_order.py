"""inherited sale order"""
from odoo import models, fields


class SaleOrder(models.Model):
    """class created for inherited sale order"""
    _inherit = 'sale.order'
    _description = "Created this module."
