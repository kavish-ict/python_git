"""
inherited view
"""

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    _description = 'Res Partner'

    ngo_check = fields.Boolean(string="NGO")
    orphan_members=fields.Integer(compute='total_orphan_members')

    def total_orphan_members(self):

        """
        counting courses 'not yet complete'
        """
        for rec in self:
            member_count = self.env['orphans.member'].search_count([])
            rec.orphan_members = member_count

    def total_available_funds(self):
        pass
        # for rec in self:
        #     amount_count = self.env['orphans.member'].search_count([])
        #     rec.orphan_members = amount_count
