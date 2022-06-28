from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = "Created this module."

    person = fields.Char(config_parameter='credit_limit.person')

