"""
new module
"""
from odoo import models, fields,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'sale order inherited'

    @api.model
    def _name_search(self,name,args=None,operator='ilike',limit=10,name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('new_mobile', operator, name), ('new_email', operator, name)]
        return self._search(domain + args,limit=limit,access_rights_uid=name_get_uid)

