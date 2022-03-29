"""
new module
"""
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    """
    sale.order inherited
    """
    _inherit = 'sale.order'
    _description = 'sale order inherited'

    customer_rank = fields.Integer(string="Customer Rank",related='partner_id.customer_rank')

    # res['test_ids'] = [(6, 0, lst)]
    # @api.model
    # def _name_search(self,name,args=None,operator='ilike',limit=10,name_get_uid=None):
    #     """
    #     function to search record with mobile number or email
    #     """
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', '|', ('name', operator, name), ('new_mobile', operator, name), ('new_email', operator, name)]
    #     return self._search(domain + args,limit=limit,access_rights_uid=name_get_uid)

    @api.onchange('customer_rank')
    def add_new_tag(self):
        for rec in self:
            ids = [10]
            if rec.customer_rank > 5:
                self.write({"tag_ids": [(6, 0, ids)]})

    def action_confirm(self):
        print("button works")
        # res_list = self.env['sale.order'].search([])
        # count = 0
        for rec in self:
            count = len(rec.order_line)
            if count > 3:
                raise UserError("you can add 3 lines per order")
            else:
                return super(SaleOrder, self).action_confirm()
