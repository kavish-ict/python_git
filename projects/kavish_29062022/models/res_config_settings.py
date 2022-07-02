from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = "Created this module."

    group_display_message = fields.Boolean(implied_group='kavish_29062022.group_display_message')

