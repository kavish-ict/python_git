from odoo import models, fields, api


class orphans_organization(models.Model):
    _name = 'orphans.organization'
    _description = 'orphans_organization'

    name = fields.Char(required=True)
    ngo_id = fields.Many2one(comodel_name='res.partner', string='NGO',
                             domain="[('ngo_check','=',True)]")
    o_image = fields.Binary()
    street1 = fields.Char(string="Address")
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    zip = fields.Char()
    country_id = fields.Many2one('res.country')

    # available_fund = fields.Integer(string="Available Funds")
    foundation_years = fields.Selection(selection="foundation_y", string="Foundation Year")

    # orphan_member = fields.Char(string='Orphan Member')
    @api.onchange('state_id')
    def onchange_country(self):
        self.country_id = self.state_id.country_id

    def foundation_y(self):
        x = [(str(i), i) for i in range(1990, 2022)]
        return x
        # return tuple(enumerate(x))

    def tempSmartButton(self):
        pass

    def tempSmartButton2(self):
        pass

    def name_get(self):
        """Function To Concatenate Name, NGO, State fields."""
        res = []
        for rec in self:
            if rec.state:
                res.append((rec.id, '%s (%s, %s)' % (rec.name, rec.ngo_id.name, rec.state_id)))
            else:
                res.append((rec.id, '%s (%s)' % (rec.name, rec.nago_id.name)))
        return res
