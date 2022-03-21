from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_checked = fields.Boolean("Name check")
    name_char = fields.Char(string="Name")

    is_active = fields.Boolean(string='Active', config_parameter='rental_management.active')

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #
    #     res['is_checked'] = self.env['ir.config_parameter'].get_param(
    #         'rental_management.is_checked')
    #     res['name_char'] = self.env['ir.config_parameter'].get_param(
    #         'name_char')
    #
    #     return res
    #
    # @api.model
    # def set_values(self):
    #     self.env['ir.config_parameter'].set_param(
    #         'rental_management.is_checked', self.is_checked)
    #     self.env['ir.config_parameter'].set_param(
    #         'name_char', self.test_char)
    #     super(ResConfigSettings, self).set_values()
