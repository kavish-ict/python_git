"""
new module
"""
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    """
    class created for res config settings
    """
    _inherit = 'res.config.settings'
    _description = "Created this module."

    name = fields.Char(string="name")
    # group_question_paper = fields.Boolean(string="Paper 1", implied_group='exam_2.group_question_paper')
    # question_paper_id = fields.Boolean(string="Paper 1")
    question_paper_1 = fields.Boolean(string="Paper 2")
    orders_ids = fields.Many2many("sale.order", string="Orders")

    # @api.model
    # def set_values(self):
    #     """
    #     function to set values
    #     """
    #     res = super(ResConfigSettings, self).set_values()
    #     print("-------------------set values", res)
    #     r = self.env['ir.config_parameter'].set_param('exam_2.orders_ids', self.orders_ids.ids)
    #     print("-------------", r)
    #     return res
    #
    # @api.model
    # def get_values(self):
    #     """
    #     function to get values
    #     """
    #     res = super(ResConfigSettings, self).get_values()
    #     print("-------------------get values", res)
    #     order_save = self.env['ir.config_parameter'].get_param('exam_2.orders_ids')
    #     res.update(
    #         orders_ids=[(6, 0, eval(order_save))] if order_save else False)
    #     return res

