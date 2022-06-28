from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = "Created this module."

    credit_limit = fields.Boolean('Credit Limit')
    block_limit = fields.Boolean('Blocking Limit')
    credit_limit_score = fields.Float('Credit Limit Score')
    block_limit_score = fields.Float('Blocking Limit Score')


