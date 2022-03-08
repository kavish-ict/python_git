from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CusRef(models.Model):
    _inherit = 'res.partner'

    customer_ref_no = fields.Integer(string="ref.no")
