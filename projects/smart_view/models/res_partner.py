from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s -- %s' % (rec.name, rec.customer_ref_no)))
        return res

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=10, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

