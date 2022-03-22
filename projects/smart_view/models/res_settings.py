""" this model is for config setting"""
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    """
    res.config.settings inherited
    """
    _inherit = 'res.config.settings'

    is_checked = fields.Boolean("Name check")
    name_char = fields.Char(string="Name")
    name_id = fields.Many2one('hr.employee',string="Company",config_parameter="smart.view.name_id")

    @api.model
    def get_values(self):
        """
        function to get the values in res.config.settings
        """
        res = super(ResConfigSettings, self).get_values()
        res['is_checked'] = self.env['ir.config_parameter'].get_param(
            'rental_management.is_checked')
        res['name_char'] = self.env['ir.config_parameter'].get_param(
            'name_char')
        # res['name_id'] = self.env['ir.config_parameter'].get_param(
        #     'name_id')
        return res

    @api.model
    def set_values(self):
        """
        function to set values in res.config.settings
        """
        self.env['ir.config_parameter'].set_param(
            'rental_management.is_checked', self.is_checked)
        self.env['ir.config_parameter'].set_param(
            'name_char', self.name_char)
        # self.env['ir.config_parameter'].set_param(
        #     'name_id', self.name_id.id)
        super(ResConfigSettings, self).set_values()

    @api.onchange("is_checked")
    def onchange_is_checked(self):
        """
        function to set empty value in html field and many2one when checkbox is checked again
        """
        for rec in self:
            if not rec.is_checked:
                rec.name_char = False
                rec.name_id = False
