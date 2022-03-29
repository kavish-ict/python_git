
from odoo import models , fields , api

class orphans_donation(models.Model):

    _name = 'orphans.organization.donation'
    _description = 'orphans_donation'

    name = fields.Char(required=True , string="Doner Name")
    organization_id = fields.Many2one('orphans.organization', string="Orphans Home")
    amount = fields.Integer(string="Amount", required=True)
    phone = fields.Char(string="Phone No")
    email = fields.Char(string="Email")

    s1 = fields.Char(string="Address")
    s2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    zip = fields.Char()
    country_id = fields.Many2one('res.country')

    @api.onchange('state_id')
    def onchange_country(self):
        print("\n -------------------------------------------",self.state_id.id)
        self.country_id = self.state_id.country_id

    def s_button(self):
        pass


