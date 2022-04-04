"""
new module
"""
from odoo import models, fields, api


class HrWizard(models.Model):
    """
    class rental management with inherited model
    """
    _name = 'hr.wizard'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "create new object for rental"
    # _rec_name = 'name'

    employee = fields.Char(string="Employee")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")