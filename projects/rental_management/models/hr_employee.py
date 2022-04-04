"""
new module
"""
from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = "inherit product template object"

    test = fields.Integer(string="AGE")

