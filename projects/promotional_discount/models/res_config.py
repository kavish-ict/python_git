from odoo import models, fields, api, _


class ResConfigSetting(models.TransientModel):
    _inherit = "res.config.settings"
    _description = "Res Config Settings"

    group_discount_check = fields.Boolean(string="Promotional Discount",
                                          implied_group="promotional_discount.group_promotional_discount")
