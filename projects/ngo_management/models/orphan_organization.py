

from odoo import models, fields, api


class orphans_organization(models.Model):

    _name = 'orphans.organization'
    _description = 'orphans_organization'

    name = fields.Char(required=True)
    o_image = fields.Binary()
    ngo_id = fields.Many2one(comodel_name='res.partner', string='NGO',
                             domain="[('ngo_check','=',True)]")
    street1 = fields.Char(string="Address")
    street2 = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip = fields.Char()
    country = fields.Char()

    # available_fund = fields.Integer(string="Available Funds")
    foundation_years = fields.Selection(selection="foundation_y", string="Foundation Year")
    # orphan_member = fields.Char(string='Orphan Member')

    def foundation_y(self):
        x = [(str(i), i) for i in range(1990, 2022)]
        return x
        # return tuple(enumerate(x))

    def tempSmartButton(self):
        pass

    def tempSmartButton2(self):
        pass



