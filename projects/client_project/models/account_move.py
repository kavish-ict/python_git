from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = "Created this module."

    def generate_bill(self):
        print("bill--------------------------------------")
