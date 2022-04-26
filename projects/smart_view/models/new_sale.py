from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleNew(models.Model):
    _inherit = 'sale.order'

    customer_ref_no = fields.Integer(string="ref.no", related='partner_id.customer_ref_no')
