from odoo import models, fields, api


class AdvanceActions(models.Model):
    _name = 'advance.actions'
    _description = 'advance actions'

    name = fields.Char(string="Name")
