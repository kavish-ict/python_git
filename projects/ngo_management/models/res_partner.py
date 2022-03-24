"""
inherited view
"""

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    _description = 'Res Partner'

    ngo_check = fields.Boolean(string="NGO")


    def tempSmartButton(self):
        pass


    def tempSmartButton2(self):
        pass
